# Fake Data Generator

## Ambiente Virtual
```
alias python=python3.12
alias pip=pip3.12
pip install virtualenv --user
mkdir fakedatagenerator
cd fakedatagenerator
virtualenv venv --python=python3.12
source venv/bin/activate
pip install -r requirements.txt
```

## Install ollama linux os
```
https://github.com/ollama

curl -fsSL https://ollama.com/install.sh | sh
systemctl enable ollama
systemctl start ollama


ollama run llama3.2
ollama run deepseek-r1
ollama list
ollama ps
ollama stop llama3.2
ollama stop deepseek-r1
```

-----------------


## Create container to MariaDB
```
docker run \
    --name mariadb \
    -e MYSQL_ROOT_PASSWORD=root \
    -e MARIADB_USER=fakedatagenerator \
    -e MARIADB_PASSWORD=fakedatagenerator \
    -e MARIADB_DATABASE=fakedatagenerator \
    -e TZ=America/Sao_Paulo \
    -p 3306:3306 \
    -v /media/rkumabe/DATA/workspaces/python/fakedatagenerator/infra/docker/mariadb/data:/var/lib/mysql \
    -d mariadb
```


```
docker exec -it mariadb mariadb -ufakedatagenerator -p


CREATE TABLE customers (
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(80) NOT NULL,
    last_name VARCHAR(80) NOT NULL,
    email_address VARCHAR(160) NOT NULL,
    age INT NOT NULL,
    city VARCHAR(100) NOT NULL,
    occupation VARCHAR(100) NOT NULL,
    CONSTRAINT PK_CUSTOMERS PRIMARY KEY (id)
);

docker cp fake_data.csv mariadb:/tmp/fake_data.csv
docker exec -it mariadb bash
LOAD DATA LOCAL INFILE '/tmp/fake_data.csv' INTO TABLE customers FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
```