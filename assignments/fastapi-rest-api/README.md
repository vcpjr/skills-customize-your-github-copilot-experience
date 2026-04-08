# 📘 Tarefa: APIs REST com FastAPI

## 🎯 Objective

Crie uma API REST usando FastAPI para gerenciar um catálogo simples de itens. Pratique rotas, modelos Pydantic e operações CRUD usando armazenamento em memória.

## 📝 Tasks

### 🛠️ Configurar a aplicação FastAPI

#### Descrição
Configure um aplicativo FastAPI e crie a rota inicial para validar que o servidor está funcionando.

#### Requisitos
O programa completo deve:

- Importar `FastAPI` do pacote `fastapi`
- Declarar `app = FastAPI()`
- Criar a rota `GET /` que retorne uma mensagem JSON de boas-vindas
- Iniciar o servidor com `python starter-code.py`


### 🛠️ Modelos e endpoints CRUD

#### Descrição
Defina um modelo Pydantic `Item` e implemente rotas para criar, ler, atualizar e excluir itens.

#### Requisitos
O programa completo deve:

- Criar a classe `Item` com os campos: `id`, `name`, `description`, `price` e `available`
- Implementar as rotas:
  - `GET /items/` para listar todos os itens
  - `GET /items/{item_id}` para retornar um item específico
  - `POST /items/` para adicionar um novo item
  - `PUT /items/{item_id}` para atualizar um item existente
  - `DELETE /items/{item_id}` para remover um item
- Usar uma lista em memória para armazenar os itens durante a execução


### 🛠️ Testar a API

#### Descrição
Teste a API com requisições HTTP usando o navegador, `curl` ou uma ferramenta como Postman.

#### Requisitos
O programa completo deve:

- Confirmar que `GET /items/` retorna a lista de itens
- Criar um item com `POST /items/`
- Atualizar um item com `PUT /items/{item_id}`
- Excluir um item com `DELETE /items/{item_id}`
