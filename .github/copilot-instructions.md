# Copilot Instructions

## Estilo de Código
- Siga o padrão PEP 8 para todas as sugestões de código Python.
- Utilize indentação de 4 espaços.
- Nomes de variáveis devem ser em snake_case.
- Nomes de classes devem ser em CamelCase.
- Comentários devem ser claros e úteis, preferencialmente em português.
- Linhas com no máximo 79 caracteres, sempre que possível.

## Boas Práticas
- Prefira usar `with` para manipulação de arquivos e contextos.
- Use f-strings para formatação de strings (Python 3.6+).
- Evite imports desnecessários; organize-os em blocos: built-ins, libs externas, libs internas.
- Escreva funções curtas e bem definidas, cada uma com uma única responsabilidade.
- Documente funções com docstrings no estilo Google ou NumPy.
- Valide entradas e trate exceções de forma clara e explícita.
- Use tipagem estática (type hints) sempre que possível.

## Estrutura do Projeto
- Mantenha a estrutura organizada em pacotes (`__init__.py`) com separação por domínio/responsabilidade.
- Use `src/` como diretório base do código-fonte.
- Testes devem ficar em `tests/`, com nomes correspondentes aos módulos testados.
- Utilize `pytest` como framework de testes.

## Testes
- Escreva testes unitários para cada função pública.
- Use mocks para dependências externas.
- Prefira `assert` simples e legíveis.

## Linters e Ferramentas
- Use `black` para formatação automática.
- Use `flake8` ou `ruff` para análise estática.
- Use `mypy` para verificação de tipagem estática.

## Observações
- Sempre prefira clareza e legibilidade ao invés de "clever code".
- Sugestões devem ser coesas com o restante do código existente no projeto.
