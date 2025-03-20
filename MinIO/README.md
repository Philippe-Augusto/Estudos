# minIO Documentation


## Instalação do docker:

Ubuntu:
```sh
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Referencia: [Instalando docker no ubuntu](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

## Deploy do servidor MinIO utilizando o Docker:

```sh
docker pull bitnami/minio:2024.5.10
```

Iremos utilizar o docker-compose para fazer o deploy do minIO

```yaml
services:
  minio-server:
    image: bitnami/minio:2024.5.10
    container_name: minio-server
    volumes:
      - /home/philippe/minIO/data:/bitnami/minio/data
    restart: always
    environment:
      MINIO_ROOT_USER: admin
      MINIO_ROOT_PASSWORD: admin123
    ports:
      - "9000:9000"
      - "9001:9001"
```

```sh
docker compose -f docker-compose-server.yaml up -d
```

Verifique se o container esta rodando com:
```sh
docker ps
```

Acesse a interface web em:
```link
http://localhost:9000/
```

## Deploy de 4 servidores MinIO utilizando o Docker:

> 📌 **Nota:** Não é possível fazer o deploy de menos de 4 servidores no MinIO, por isso 

```sh
docker pull bitnami/minio:2024.5.10
```

Iremos utilizar o docker-compose para fazer o deploy dos servidores

Este é um exemplo de configuração de 1 servidor, no repositório temos o yaml de configuração com os 4 servidores
```yaml
services:
  minio1:
    image: bitnami/minio:2024.5.10
    container_name: minio1
    command: minio server --address ":9000" --console-address ":9001" http://minio{1...4}/data
    volumes:
      - /home/philippe/minIO/servers/minio1_data:/data
    environment:
      MINIO_ROOT_USER: admin
      MINIO_ROOT_PASSWORD: admin123
      MINIO_DISTRIBUTED_MODE_ENABLED: yes
      MINIO_DISTRIBUTED_NODES: http://minio1:9000 http://minio2:9000 http://minio3:9000 http://minio4:9000
      MINIO_SCHEME: http
      TZ: "America/Sao_Paulo"
    ports:
      - "9000:9000"
      - "9001:9001"
    networks:
      - 

networks:
  servers_minio-net:
    driver: bridge
```



## Testando o deploy dos servidores

Configurar o MinIO Client - [Veja mais detalhes aqui](./minio-client/README.md)
```yaml
services:
  minio-client:
    image: bitnami/minio-client:latest
    container_name: minio-client
    environment:
      MINIO_SERVER_HOST: "minio1"
      MINIO_SERVER_ACCESS_KEY: "admin"
      MINIO_SERVER_SECRET_KEY: "admin123"
    networks:
      - minio-net
    command: ["sleep", "infinity"]

networks:
  minio-net:
    external: true
```

Execute o container com:
```sh
docker exec -it minio-client /bin/sh
```

Execute esses comandos no container do minio-client
```sh
mc alias set minio http://minio1:9000 admin admin123

mc admin info minio
```

Se voce obter uma saida como essa:
```
$ mc admin info minio
●  minio1:9000
   Uptime: 2 hours 
   Version: 2024-05-10T01:41:38Z
   Network: 4/4 OK 
   Drives: 1/1 OK 
   Pool: 1

●  minio2:9000
   Uptime: 2 hours 
   Version: 2024-05-10T01:41:38Z
   Network: 4/4 OK 
   Drives: 1/1 OK 
   Pool: 1

●  minio3:9000
   Uptime: 2 hours 
   Version: 2024-05-10T01:41:38Z
   Network: 4/4 OK 
   Drives: 1/1 OK 
   Pool: 1

●  minio4:9000
   Uptime: 2 hours 
   Version: 2024-05-10T01:41:38Z
   Network: 4/4 OK 
   Drives: 1/1 OK 
   Pool: 1
┌──────┬────────────────────────┬─────────────────────┬──────────────┐
│ Pool │ Drives Usage           │ Erasure stripe size │ Erasure sets │
│ 1st  │ 19.0% (total: 889 GiB) │ 4                   │ 1            │
└──────┴────────────────────────┴─────────────────────┴──────────────┘

1.3 KiB Used, 1 Bucket, 1 Object
4 drives online, 0 drives offline, EC:2
```
Parabens! Voce fez o deployment do MinIO

