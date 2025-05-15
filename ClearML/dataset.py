from clearml import Dataset

# Criar o dataset
dataset = Dataset.create(
    dataset_name="meu_dataset",
    dataset_project="meu_projeto",
    description="Dataset com arquivos do MinIO local",
    output_uri="s3://localhost:9000/clearml"  # Ou "s3://localhost:9000/clearml-data" se rodar no host
)

# Adicionar arquivos externos do bucket MinIO
(
    source_url="s3://localhost:9000/clearml",  # Caminho no bucket MinIO
    wildcard="*.png",  # Opcional: apenas arquivos JPG
    #dataset_path="/imagens",  # Caminho relativo no dataset
    recursive=True,  # Incluir subdiretórios
    verbose=True  # Mostrar logs
)

# Sincronizar e finalizar
dataset.upload()  # Envia metadados ao ClearML
dataset.finalize(verbose=True, auto_upload=True)  # Fecha o dataset
print(f"Dataset criado com ID: {dataset.id}")
