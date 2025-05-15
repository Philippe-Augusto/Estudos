from clearml import PipelineDecorator, Task, Dataset
from minio import Minio
import os
import shutil
import tempfile

# Configurações globais
MINIO_ENDPOINT = "localhost:9000"
MINIO_ACCESS_KEY = "admin"
MINIO_SECRET_KEY = "admin123"
CLEARML_PROJECT = "MyPipelineProject"
CLEARML_TASK_NAME = "DataPipeline"

# Função para baixar dados do MinIO ou ClearML Data
@PipelineDecorator.component(return_values=["local_data_path"], cache=True)
def download_data(data_source: str, data_id: str) -> str:
    """
    Baixa dados do MinIO ou ClearML Data para um diretório local.
    Args:
        data_source: 'minio' ou 'clearml_data'
        data_id: ID do dataset (ClearML) ou caminho do objeto (MinIO)
    Returns:
        Caminho local onde os dados foram salvos
    """
    task = Task.current_task()
    local_dir = tempfile.mkdtemp()  # Cria diretório temporário

    if data_source == "minio":
        # Conexão com MinIO
        client = Minio(
            "localhost:9000",
            access_key="admin",
            secret_key="admin123",
            secure=False
        )
        # Supondo que data_id é o caminho do objeto no MinIO (ex.: bucket/path/to/file)
        bucket_name, object_path = data_id.split("/", 1)
        objects = client.list_objects(bucket_name, prefix=object_path, recursive=True)
        for obj in objects:
            local_file = os.path.join(local_dir, obj.object_name.replace(object_path, ""))
            os.makedirs(os.path.dirname(local_file), exist_ok=True)
            client.fget_object(bucket_name, obj.object_name, local_file)
            task.get_logger().report_text(f"Downloaded {obj.object_name} to {local_file}")

    elif data_source == "clearml_data":
        # Baixa dataset do ClearML Data
        dataset = Dataset.get(dataset_id=data_id)
        local_dir = dataset.get_local_copy()  # ClearML gerencia o download
        task.get_logger().report_text(f"Downloaded ClearML Dataset {data_id} to {local_dir}")

    else:
        raise ValueError("data_source must be 'minio' or 'clearml_data'")

    return local_dir

# Função genérica de processamento (ex.: treinamento/inferência)
@PipelineDecorator.component(return_values=["output_dir"], cache=True)
def process_data(local_data_path: str) -> str:
    """
    Processa os dados no diretório local e gera resultados.
    Args:
        local_data_path: Caminho local com os dados baixados
    Returns:
        Diretório com os resultados
    """
    task = Task.current_task()
    output_dir = tempfile.mkdtemp()  # Diretório para resultados

    # Exemplo: Simula processamento criando um arquivo de saída
    output_file = os.path.join(output_dir, "result.txt")
    with open(output_file, "w") as f:
        f.write(f"Processed data from {local_data_path}")
    
    task.get_logger().report_text(f"Processed data and saved results to {output_dir}")
    return output_dir

# Função para fazer upload de dados para MinIO ou ClearML Data
@PipelineDecorator.component(return_values=["uploaded_data_id"], cache=True)
def upload_data(output_dir: str, upload_destination: str, dataset_name: str = None) -> str:
    """
    Faz upload dos dados para MinIO ou cria nova versão no ClearML Data.
    Args:
        output_dir: Diretório com os dados a serem enviados
        upload_destination: 'minio' ou 'clearml_data'
        dataset_name: Nome do dataset no ClearML (opcional, para clearml_data)
    Returns:
        ID ou caminho dos dados enviados
    """
    task = Task.current_task()
    uploaded_data_id = ""

    if upload_destination == "minio":
        # Conexão com MinIO
        client = Minio(
            "localhost:9000",
            access_key="admin",
            secret_key="admin123",
            secure=False
        )
        bucket_name = "clearml"  # Defina o bucket
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)

        # Faz upload de todos os arquivos no diretório
        for root, _, files in os.walk(output_dir):
            for file in files:
                file_path = os.path.join(root, file)
                object_name = os.path.relpath(file_path, output_dir)
                client.fput_object(bucket_name, object_name, file_path)
                task.get_logger().report_text(f"Uploaded {file_path} to {bucket_name}/{object_name}")
        uploaded_data_id = f"{bucket_name}/{object_name}"

    elif upload_destination == "clearml_data":
        # Cria uma nova versão no ClearML Data
        dataset = Dataset.create(
            dataset_name=dataset_name or "ProcessedDataset",
            dataset_project="MyPipelineProject",
            parent_datasets=None
        )
        dataset.add_files(output_dir)
        dataset.upload()
        dataset.finalize()
        uploaded_data_id = dataset.id
        task.get_logger().report_text(f"Created ClearML Dataset {uploaded_data_id}")

    else:
        raise ValueError("upload_destination must be 'minio' or 'clearml_data'")

    return uploaded_data_id

# Definindo o Pipeline
@PipelineDecorator.pipeline(
    name="DataProcessingPipeline",
    project="MyPipelineProject",
    version="1.0"
)
def data_pipeline(data_source: str, data_id: str, upload_destination: str, dataset_name: str = None):
    """
    Pipeline principal que orquestra download, processamento e upload de dados.
    Args:
        data_source: 'minio' ou 'clearml_data'
        data_id: ID ou caminho dos dados
        upload_destination: 'minio' ou 'clearml_data'
        dataset_name: Nome do dataset no ClearML (opcional)
    """
    # Etapa 1: Download dos dados
    local_data_path = download_data(data_source, data_id)
    
    # Etapa 2: Processamento
    output_dir = process_data(local_data_path)
    
    # Etapa 3: Upload dos resultados
    uploaded_data_id = upload_data(output_dir, upload_destination, dataset_name)
    
    return uploaded_data_id

# Executando o Pipeline
if __name__ == "__main__":
    # Habilita o pipeline decorator
    PipelineDecorator.set_default_execution_queue("default")
    PipelineDecorator.run_locally()

    # Exemplo de execução
    data_pipeline(
        data_source="minio",
        data_id="clearml/",  # Substitua pelo ID real
        upload_destination="clearml_data",
        dataset_name="meu_dataset"
    )
