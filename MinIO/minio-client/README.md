# MinIO Client

## Deploy
> 📌 **Nota:** Estamos utilizando a imagem da bitnami (ela suporta multi node multi driver).

Configurar um yaml para utilizar um docker compose
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
      - servers_minio-net # Certifique-se de que o container esteja na mesma rede que os containeres dos servidores
    command: ["sleep", "infinity"] # Isso faz com que o container não encerre após ele iniciar

networks:
  servers_minio-net:
    external: true
```

Deploy do container
```sh
docker compose -f docker-compose-client.yaml up -d 
```

## Configuração/Testes

Verificar se o container esta rodando
```sh
docker ps
```

Conectar ao servidor (Caso você tenha feito o deploy dos servidores)
```sh
docker exec -it minio-client /bin/sh
```

```sh
mc alias set minio http://minio1:9000 admin admin123
mc admin info minio
```

Saída esperada:
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
