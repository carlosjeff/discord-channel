# Discord Channel

Sistema que detecta quando você entra em um canal do discord e manda uma "mensagem" para a fila do Kafka

## Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### Pré-requisitos

* Python
* pipenv
* Docker

### Instalação

Clone este repositório usando o comando:
```bash
$ git clone https://github.com/carlosjeff/discord-channel.git

```
Na pasta do projeto instale as dependências com uso do npm
```bash
$ pipenv install
$ pipenv shell
```
No arquivo [.env](https://github.com/carlosjeff/people-crud-api/blob/main/.env) edite os dados de conexão com o banco de dados:
```
TOKEN_DISCORD="Token do bot do Discord"
```

Para iniciar o servidor é só usar o comando na pasta do projeto:
```bash
$ python main.py

```


Para iniciar o servidor Usando o Docker
```bash
$ docker compose up -d
```

## Construído com

* [Python](https://www.python.org/) - Linguagem de programação
* [kafka-python](https://kafka-python.readthedocs.io/en/master/index.html) - Biblioteca de gerenciamendo do Kafka
* [discord.py](https://kafka-python.readthedocs.io/en/master/index.html) - APi do Discord

## Autor

* **Carlos Jefferson Braga Alves** - [LinkedIn ](https://www.linkedin.com/in/carlosjeff/)


## Licença

Este projeto está sob a licença MIT License - veja o arquivo [LICENSE.md](https://github.com/carlosjeff/discord-channel/blob/main/LICENSE) para detalhes.


