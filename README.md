# Fake Data Generator

## Descrição

O **Fake Data Generator** é uma aplicação Python que utiliza o modelo de linguagem `llama3.2` para gerar dados falsos em formato CSV. Esses dados podem ser usados para testes, desenvolvimento ou outras finalidades que exijam dados fictícios.

## Estrutura do Projeto

```
├── .github/
│   ├── copilot-instructions.md
│   ├── dependabot.yaml
├── infra/
│   ├── main.tf
│   ├── docker/
│       ├── mariadb/
│           ├── data/
├── src/
│   ├── create_fake_data.py
│   ├── custom_client_async.py
│   ├── custom_client_sync.py
│   ├── fake_data_generator.py
│   ├── main.py
│   ├── ollama_chat.py
│   ├── ollama_generate.py
│   ├── processar_string.py
│   ├── streaming_responses.py
├── .gitignore
├── HOW_TO_USE.md
├── LICENSE
├── requirements.txt
```

## Requisitos

- Python 3.12+
- [Ollama](https://github.com/ollama) instalado e configurado
- Docker (para MariaDB)
- Terraform (opcional, para infraestrutura)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/fakedatagenerator.git
   cd fakedatagenerator
   ```

2. Configure o ambiente virtual:
   ```bash
   alias python=python3.12
   alias pip=pip3.12
   pip install virtualenv --user
   virtualenv venv --python=python3.12
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Instale e configure o Ollama:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   systemctl enable ollama
   systemctl start ollama
   ollama run llama3.2
   ```

4. Configure o banco de dados MariaDB (opcional):
   ```bash
   docker run \
       --name mariadb \
       -e MYSQL_ROOT_PASSWORD=root \
       -e MARIADB_USER=fakedatagenerator \
       -e MARIADB_PASSWORD=fakedatagenerator \
       -e MARIADB_DATABASE=fakedatagenerator \
       -e TZ=America/Sao_Paulo \
       -p 3306:3306 \
       -v $(pwd)/infra/docker/mariadb/data:/var/lib/mysql \
       -d mariadb
   ```

## Uso

### Gerar Dados Falsos

Execute o script principal para gerar dados falsos:
```bash
python src/main.py
```

### Outros Scripts

- `create_fake_data.py`: Gera dados falsos e salva em um arquivo CSV.
- `ollama_chat.py`: Interage com o modelo `llama3.2` em modo de chat.
- `ollama_generate.py`: Gera respostas baseadas em prompts fornecidos.
- `processar_string.py`: Converte strings de snake_case para CamelCase.

## Testes

Os testes devem ser escritos em `tests/` e executados com o `pytest`:
```bash
pytest
```

## Contribuição

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [Licença Apache 2.0](LICENSE).

## Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: `seu-email@exemplo.com`.

## Teste
Adicionei um filtro no workflow para validar se eu alterar somente os arquivos *.md o workflow não vai iniciar

```
on:
  push:
    paths-ignore:
      - '**/*.md'
```
