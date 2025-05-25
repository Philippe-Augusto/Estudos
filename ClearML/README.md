# Documentação ClearML

## Instalação via Docker-Compose
### 1. Modifique o `vm.max_map_count` no docker

Pelo terminal:
```bash
echo "vm.max_map_count=262144" > /tmp/99-clearml.conf
sudo mv /tmp/99-clearml.conf /etc/sysctl.d/99-clearml.conf
sudo sysctl -w vm.max_map_count=262144
sudo service docker restart
```

Docker desktop:

![image](https://github.com/user-attachments/assets/c51013ac-0460-4126-b703-ccff23db78ce)

### 2. Crie diretorios locais para os bancos de dados e armazenamento.
```bash
sudo mkdir -p /opt/clearml/data/elastic_7
sudo mkdir -p /opt/clearml/data/mongo_4/db
sudo mkdir -p /opt/clearml/data/mongo_4/configdb
sudo mkdir -p /opt/clearml/data/redis
sudo mkdir -p /opt/clearml/logs
sudo mkdir -p /opt/clearml/config
sudo mkdir -p /opt/clearml/data/fileserver
```

```bash
sudo chown -R 1000:1000 /opt/clearml
```

> ⚠️ **Atenção:** Caso você utilize um endereço diferente de `localhost:8080` para o webserver do ClearML, defina este endereço com:
```bash
export CLEARML_HOST_IP=server_host_ip_here
```

### 3. Execute o compose
Docker compose disponível em: [docker-compose](./docker-compose.yaml)
```
docker compose -f docker-compose.yaml up -d
```

### 4. Defina as variáveis de ambiente:

Acesse: `http://<YOUR_CLEARML_HOST_IP:8080/settings/workspace-configuration`

Clique em create new credentials, agora exporte as credenciais de acesso como variaveis de ambiente conforme o comando abaixo.

Mas antes de exporta-las, precisamos reiniciar os containers, faça isso com os seguintes comandos:
```bash
docker compose -f docker-compose.yaml down
```

```bash
export CLEARML_AGENT_ACCESS_KEY=generate_access_key_here
export CLEARML_AGENT_SECRET_KEY=generate_secret_key_here
```

Caso você queira utilizar que o ClearML utilize o git para acessar repositórios privados, forneça as seguintes variáveis de ambiente:
```bash
export CLEARML_AGENT_GIT_USER=git_username_here
export CLEARML_AGENT_GIT_PASS=git_password_here
```

Agora suba o ClearML novamente e verifique se o agent esta atuando como worker no ClearML
```bash
docker compose -f docker-compose.yaml up -d
```

## Manipulação básica de dados
### Requisitos
- ClearML implementado com docker-compose.
- 4 servidores MinIO implementados.

**Nota**: Certifique-se de que o ClearML e o MinIO estejam se comunicando através das redes gerenciadas pelo docker.

### Adição de arquivos ao ClearML através do MinIO
- Configure um bucket chamado clearml no MinIO e insira alguns arquivos para teste.

- Com os arquivos inseridos utilize o SDK para a criação do Dataset dentro do ClearML
```
from clearml import Dataset

dataset = Dataset.create(
    dataset_name="meu_dataset",
    dataset_project="meu_projeto",
    description="Dataset com arquivos do MinIO local",
    output_uri="s3://localhost:9000/clearml"
)

dataset.add_external_files(
    source_url="s3://localhost:9000/clearml/",
    wildcard="*.png",
    dataset_path="/imagens",
    recursive=True,
    verbose=True
)

dataset.upload()
dataset.finalize(verbose=True, auto_upload=True)
print(f"Dataset criado com ID: {dataset.id}")
```

### Utilizando o Dataset
- Script para carregar o dataset e listar os arquivos PNG:
```
from clearml import Dataset
import os

dataset = Dataset.get(dataset_project="meu_projeto", dataset_name="meu_dataset")
local_path = dataset.get_local_copy()
print(f"Dataset baixado para: {local_path}")

image_files = []
for root, _, files in os.walk(local_path):
    for file in files:
        if file.endswith(".png"):
            image_files.append(os.path.join(root, file))

print(f"Total de imagens PNG encontradas: {len(image_files)}")
for file_path in image_files:
    print(f" - {file_path}")
```

### Adição de novos arquivos
- Caso o dataset já tenha sido finalizado (com a função "dataset.finalize(verbose=True)", não é possível acrescentar novos arquivos, para isso podemos criar um dataset como subconjunto do outro,
- Caso o dataset não tenho sido finalizado, podemos utilizar a função add_files ou add_external_files, a depender de onde o arquivo está

## Dataset com subconjunto de outro dataset
- No clearML é possível criar datasets selecionando um subconjunto do primeiro (Como um formato em específico ou até realizando uma seleção manual

- Exemplo de código que utiliza um dataset para criação de outro
```
from clearml import Dataset
import os

# Carregar o dataset original
parent_dataset = Dataset.get(dataset_project="meu_projeto", dataset_name="meu_dataset")
print(f"Dataset original carregado: {parent_dataset.id}")

# Criar um novo dataset como filho do dataset original
new_dataset = Dataset.create(
    dataset_name="meu_dataset_subconjunto",
    dataset_project="meu_projeto",
    parent_datasets=[parent_dataset.id],  # Vincula ao dataset original
    description="Subconjunto do dataset original com arquivos PNG selecionados",
    output_uri="s3://localhost:9000/clearml"  # Mesmo bucket, apenas referências
)

# Obter o caminho local do dataset original
local_path = parent_dataset.get_local_copy()
print(f"Dataset original baixado para: {local_path}")

# Selecionar um subconjunto de arquivos (exemplo: até 2 arquivos PNG)
selected_files = []
file_count = 0
max_files = 2  # Limite de arquivos para o subconjunto
for root, _, files in os.walk(local_path):
    for file in files:
        if file.endswith(".png"):
            file_path = os.path.join(root, file)
            # Converter o caminho local para o caminho relativo no dataset
            relative_path = os.path.relpath(file_path, local_path)
            selected_files.append(relative_path)
            file_count += 1
            if file_count >= max_files:
                break
    if file_count >= max_files:
        break

# Adicionar os arquivos selecionados ao novo dataset
for relative_path in selected_files:
    # O arquivo já está no bucket original, então apenas referenciamos
    new_dataset.add_files(
        path=os.path.join(local_path, relative_path),
        dataset_path=relative_path,  # Manter o mesmo caminho relativo
        verbose=True
    )

# Finalizar o dataset
new_dataset.upload()
new_dataset.finalize(verbose=True, auto_upload=True)
print(f"Novo dataset criado com ID: {new_dataset.id}")
print(f"Arquivos adicionados: {selected_files}")
```
