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
