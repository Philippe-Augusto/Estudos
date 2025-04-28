# Esta seção contem um guia para o deploy local do Nextcloud

## Deploy do servidor
- Crie o docker-compose.yaml
```yaml
services:
  db:
    image: mariadb
    restart: always
    command: --transaction-isolation=READ-COMMITTED --binlog-format=ROW
    environment:
      - MYSQL_ROOT_PASSWORD=senha_raiz
      - MYSQL_PASSWORD=senha_nextcloud
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
    volumes:
      - db:/var/lib/mysql

  app:
    image: nextcloud
    ports:
      - 8080:80
    links:
      - db
    volumes:
      - nextcloud:/var/www/html
    environment:
      - MYSQL_PASSWORD=senha_nextcloud
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_HOST=db

volumes:
  db:
  nextcloud:
```

## Sincronização de pasta com o servidor Nextcloud

### Instalando o client nextcloud
```sh
sudo apt update 
sudo apt install nextcloud-desktop-cmd -y
```

### Versao Grafica
```sh
sudo apt install nextcloud-desktop
```

### Criando a pasta
```sh
mkdir ~/nextcloud_sync
```

### Sincronizando via CLI
```sh
nextcloudcmd ~/nextcloud_sync http://localhost:8080
```

### Sicnronizando via interface gráfica
- Insira o URL do servidor

![image](https://github.com/user-attachments/assets/392b9e5c-329a-4f36-87a9-43380c516326)

- Configurando a sincronização
  
![image](https://github.com/user-attachments/assets/afe3df6b-061d-4e31-a090-c6665fbf1f24)

Agora ao inserirmos um arquivo no servidor, o cliente realiza a sincronização de forma automática.


### Checando a sincronização

![image](https://github.com/user-attachments/assets/acd45257-de04-4dff-92a7-a5a9399508f7)




