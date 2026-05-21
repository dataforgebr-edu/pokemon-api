# Pokemon API

Projeto em Python que consulta a [PokeAPI](https://pokeapi.co/) e exibe informações de pokemons aleatórios no terminal.

## O que faz

Busca 10 pokemons aleatórios (IDs entre 1 e 100) e imprime o nome e tipos de cada um. 

```
Pokemon=bulbasaur - types=grass, poison
Pokemon=charizard - types=fire, flying
...
```

## Requisitos

- Python 3.12+
- [Poetry](https://python-poetry.org/)

## Instalação

```bash
poetry install
```

## Uso

```bash
poetry task app
```

## Docker

### Build da imagem

```bash
docker build -t pokemon-api .
```

### Rodando o container

```bash
# Exibe os prints em tempo real
docker run --name meu-pokemon-api pokemon-api

# Roda em background
docker run -d --name meu-pokemon-api pokemon-api
```

### Logs

```bash
# Ver logs
docker logs meu-pokemon-api

# Acompanhar em tempo real
docker logs -f meu-pokemon-api
```

### Gerenciamento

```bash
docker stop meu-pokemon-api
docker rm meu-pokemon-api
```

## Desenvolvimento

### Comandos disponíveis

| Comando | Descrição |
|---|---|
| `poetry task app` | Roda a aplicação |
| `poetry task lint` | Formata o código (black + isort) |
| `poetry task lint-check` | Verifica formatação sem alterar |
| `poetry task security` | Scan de segurança (bandit) |
| `poetry task test` | Roda os testes |

### Qualidade de código

O projeto usa [pre-commit](https://pre-commit.com/) com as seguintes verificações automáticas a cada commit:

- **black** — formatação de código
- **isort** — ordenação de imports
- **bandit** — análise de segurança

Para instalar os hooks:

```bash
poetry run pre-commit install
```
