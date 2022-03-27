# RegisterClient

Aplicação de registro de usuários e clientes utilizando o conceito Clean Code.



## Tecnologias

- Python 3.10
- Flask
- Sql Alchemy
- Pytest


## Documentação da API

```http
  POST/users
```
#### Retorna o objeto criado

| Parâmetro   | Tipo       | Descrição                                    |
| :---------- | :--------- | :--------------------------------------------|
| `dataUser ` | `object` | **Obrigatório**. Dados de registro do usuário  |

```http
  GET/users
```
#### Retorna o objeto do id correspondente

| Parâmetro   | Tipo       | Descrição                                    |
| :---------- | :--------- | :--------------------------------------------|
| `user_id`   | `int`      | **Obrigatório**. ID do usuário               |


```http
  POST/clients
```
#### Retorna o objeto criado

| Parâmetro   | Tipo       | Descrição                                    |
| :---------- | :--------- | :--------------------------------------------|
| `dataClient` | `object` | **Obrigatório**. Dados de registro do cliente |


```http
  GET/clients
```
#### Retorna o objeto do id correspondente

| Parâmetro   | Tipo       | Descrição                                    |
| :---------- | :--------- | :--------------------------------------------|
| `client_id` | `int`      | **Obrigatório**. ID do cliente               |
