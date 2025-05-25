# Documentação ClearML

Esta documentação tem como objetivo orientar a instalação e configuração do ClearML Server utilizando o Docker Compose, de forma prática e organizada. Além disso, será documentado a manipulação básica de um dataset no ClearML.
Ao seguir os passos abaixo, você será capaz de levantar uma instância completa do ClearML Server localmente, incluindo seus principais serviços: MongoDB, Elasticsearch, Redis, e o próprio servidor ClearML. A instalação utiliza diretórios persistentes para garantir a integridade dos dados e permite a personalização por meio de variáveis de ambiente.

Este guia assume que você já possui o Docker e o Docker Compose instalados no seu ambiente. Caso contrário, recomenda-se instalar essas ferramentas antes de prosseguir.

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

### 4. Crie seu usuário e gere as chaves de acesso
Acesse: `http://<YOUR_CLEARML_HOST_IP:8080`

- Crie uma conta de administrador preenchendo os campos solicitados.

- Após o login, vá até o canto superior direito e clique no seu usuário.

- Acesse "Settings" > "Workers & Queues" > "Create new credentials".

- Copie a Access Key e a Secret Key geradas — você irá usá-las nas variáveis de ambiente.


### 5. Defina as variáveis de ambiente:

Pare os containers, faça isso com os seguinte comando:
```bash
docker compose -f docker-compose.yaml stop
```

Agora vamos criar um arquivo `.env` na pasta onde esta o seu docker compose, o arquivo deve ser semelhante a esse:
```env
CLEARML_AGENT_ACCESS_KEY=9MF85ZJ4ISB1GI1TH4XP8DTT7AXU2E
CLEARML_AGENT_SECRET_KEY=zF4Tiqs7XcHMQFxtrgF5-wcMM_5Viipbfjh5Y6XD5KmGb-_1NwPfnj7Ain9fHij1qmQ
CLEARML_HOST_IP=127.0.0.1
```

Caso você queira utilizar que o ClearML utilize o git para acessar repositórios privados, acrescente as seguintes variáveis de ambiente no arquivo `.env`:
```bash
CLEARML_AGENT_GIT_USER=git_username_here
CLEARML_AGENT_GIT_PASS=git_password_here
```

Agora suba o ClearML novamente e verifique se o agent esta atuando como worker no ClearML
```bash
docker compose -f docker-compose.yaml start
```

## Manipulação básica de dados

### **Configurar o ClearML**
Configure o ClearML localmente:
```bash
clearml-init
```

- Siga as instruções para configurar as credenciais, que podem ser encontradas no ClearML UI.
- O arquivo de configuração (`~/clearml.conf`) deve ser semelhante a:
  
```yaml
api {
    web_server: http://localhost:8080
    api_server: http://localhost:8008
    files_server: http://localhost:8081
    credentials {
        "access_key" = "II7W101CXRA6B3UTJLEBUO2WJTZR3T"
        "secret_key" = "Yj6ax0n7dh0Dt_5X06qcAlzWQJ3rPbXP8BMmqSZ_TW2M4YYOrw2ftni7AfvYgDTdo-8"
    }
}
sdk {
    aws {
        s3 {
            credentials: [
                {
                    host: "localhost:9000"
                    bucket: "clearml"
                    key: "admin"
                    secret: "admin123"
                    multipart: false
                    secure: false
                    verify: false
                }
            ]
        }
    }
    development {
        default_output_uri: "s3://localhost:9000/clearml"
    }
}
```

No repositório tem um jupyter notebook, mostrando as principais funcionalidades e manipulações a serem feitas em um dataset no ClearML

[Jupyter Notebook](./clearml.ipynb)

## Conclusao

Com o ClearML Server instalado e funcionando localmente, você já pode:

- Rastrear experimentos e seus hiperparâmetros;

- Agendar e monitorar tarefas com agentes;

- Armazenar artefatos e logs de forma estruturada;

- Colaborar com outros membros da equipe de forma centralizada.

## Referencias
[ClearML Documentation](https://clear.ml/docs/latest/docs/)
