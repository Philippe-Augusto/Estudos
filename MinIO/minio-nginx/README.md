# Nesta seção terá um guia para uso do MinIO com o Nginx como proxy reverso com um certificado auto assinado

## Certificados
Como estamos no ambiente local, iremos adicionar o nosso "dominio" ao /etc/hosts

```
127.0.0.1 localhost
127.0.0.1 minio.local
```

Gere o certificado com o comando:
```sh
certgen -host "minio1,minio2,minio3,minio4,localhost,127.0.0.1"
```

Copie os arquivos "private.key" e "public.crt" para uma pasta de sua preferência para armazenar os certificados

## Configurando Nginx com certificado
Crie o arquivo "nginx.conf¨

```yaml
events {}

http {
    upstream minio_backend {
        least_conn;
        server minio1:9000;
        server minio2:9002;
        server minio3:9004;
        server minio4:9006;
    }

    upstream minio_console {
        least_conn;
        server minio1:9000;
        server minio2:9002;
        server minio3:9004;
        server minio4:9006;
    }

    server {
        listen 80;
        server_name minio.local;

        # Redirecionar todo o tráfego HTTP para HTTPS
        return 301 https://$host$request_uri;
    }

    server {
        listen 443 ssl;
        server_name minio.local;

        ssl_certificate /etc/nginx/certs/public.crt;
        ssl_certificate_key /etc/nginx/certs/private.key;

        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers on;

        # Segurança adicional (Opcional)
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

        # Configurações do proxy
        ignore_invalid_headers off;
        client_max_body_size 0;
        proxy_buffering off;
        proxy_request_buffering off;

        location / {
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            proxy_connect_timeout 300;
            #proxy_http_version 1.1;
            proxy_set_header Connection "";
            chunked_transfer_encoding off;

            proxy_pass https://minio_backend;
        }

        location /minio/ui/ {
            rewrite ^/minio/ui/(.*) /$1 break;
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-NginX-Proxy true;
            real_ip_header X-Real-IP;

            proxy_connect_timeout 300;

            #proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";

            chunked_transfer_encoding off;
            proxy_pass https://minio_console;
        }
    }
}
```

## Adicionando o Nginx ao Docker Compose
```yaml
services:
  nginx:
      image: nginx:latest
      container_name: nginx
      volumes:
        - /home/philippe/minIO/servers/nginx.conf:/etc/nginx/nginx.conf:ro
        - /home/philippe/minIO/servers/certs:/etc/nginx/certs:ro
      ports:
        - "443:443"
      depends_on:
        - minio1
        - minio2
        - minio3
        - minio4
      networks:
       - minio-net
```

Confira o Yaml completo em: (Yaml Completo)[./docker-compose-servers-nginx]

## Acessando o minio
Acesse o minio através do proxy reverso com:
```
https://minio.local
```

**Nota**: Observe que como configuramos o nginx como um "LoadBalancer", ao acessar o minio.local, o servidor que atenderá sua solicitação pode ser um dos 4 servidores disponíveis

Faça um upload de algum arquivo para teste:
![image](https://github.com/user-attachments/assets/b4605a5d-e4f8-4697-a493-a09280d59ba3)

Pare um servidor e tente acessar o MinIO:
```
https://minio.local
```
![image](https://github.com/user-attachments/assets/da593399-71fc-4423-b0c0-e9919b1903f7)

Tente fazer o download de um arquivo que voce fez o upload

Caso você consiga executar todos os passos, Parabens! Voce esta utilizando o nginx como proxy reverso para acessar o MinIO
