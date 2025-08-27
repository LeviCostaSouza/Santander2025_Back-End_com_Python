# 🛒 Store API - FastAPI com TDD

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-7.0+-green.svg)](https://www.mongodb.com/)
[![Poetry](https://img.shields.io/badge/Poetry-1.6+-orange.svg)](https://python-poetry.org/)

Uma API RESTful moderna para gerenciamento de loja construída com **FastAPI** seguindo a metodologia **TDD (Test-Driven Development)**. Projeto desenvolvido durante o bootcamp da **Digital Innovation One (DIO)**.

## 🚀 Características

- ✅ **API REST** completa com FastAPI
- ✅ **TDD (Test-Driven Development)** - Desenvolvimento orientado a testes
- ✅ **MongoDB** como banco de dados NoSQL
- ✅ **Pydantic** para validação de dados
- ✅ **Poetry** para gerenciamento de dependências
- ✅ **Documentação automática** com Swagger/OpenAPI
- ✅ **Async/Await** para operações assíncronas
- ✅ **Configurações com variáveis de ambiente**

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| Python | 3.12+ | Linguagem de programação |
| FastAPI | 0.104+ | Framework web moderno |
| MongoDB | 7.0+ | Banco de dados NoSQL |
| Motor | 3.3+ | Driver assíncrono para MongoDB |
| Pydantic | 2.5+ | Validação de dados |
| Pytest | 7.4+ | Framework de testes |
| Poetry | 1.6+ | Gerenciamento de dependências |

## 📁 Estrutura do Projeto

```
FastAPI_com_TDD/
├── 📂 store/                 # Código principal da aplicação
│   ├── 📂 core/             # Configurações e settings
│   │   └── config.py        # Configurações da aplicação
│   ├── 📂 controllers/      # Controladores/Routers
│   ├── 📂 schemas/          # Modelos Pydantic
│   ├── 📂 usecases/         # Lógica de negócio
│   ├── __init__.py
│   └── main.py              # Ponto de entrada da aplicação
├── 📂 tests/                # Testes automatizados
├── 📂 docs/                 # Documentação
├── .env                     # Variáveis de ambiente
├── docker-compose.yml       # Configuração Docker
├── Makefile                 # Scripts de automação
├── pyproject.toml          # Configuração do Poetry
└── README.md               # Este arquivo
```

## 🔧 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- [Python 3.12+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [MongoDB](https://www.mongodb.com/try/download/community) (local ou Docker)
- [Git](https://git-scm.com/downloads)

## 🚀 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/FastAPI_com_TDD.git
cd FastAPI_com_TDD
```

### 2. Configure o ambiente virtual com Poetry
```bash
# Instalar dependências
poetry install

# Ativar o ambiente virtual
poetry shell
```

### 3. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```bash
DATABASE_URL=mongodb://localhost:27017/store?uuidRepresentation=standard
```

### 4. Execute a aplicação
```bash
# Usando Poetry
poetry run uvicorn store.main:app --reload

# Ou usando Makefile
make run

# Ou diretamente
uvicorn store.main:app --reload
```

A aplicação estará disponível em: `http://127.0.0.1:8000`

## 📚 Documentação da API

Após iniciar a aplicação, acesse:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`
- **OpenAPI JSON**: `http://127.0.0.1:8000/openapi.json`

## 🧪 Executando os Testes

```bash
# Executar todos os testes
pytest

# Executar com coverage
pytest --cov=store

# Executar testes específicos
pytest tests/test_main.py

# Executar em modo watch (re-executa quando arquivos mudam)
pytest --watch
```

## 🐳 Docker

### Usando Docker Compose (Recomendado)
```bash
# Subir todos os serviços (API + MongoDB)
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar serviços
docker-compose down
```

### Usando Docker manualmente
```bash
# Build da imagem
docker build -t fastapi-store .

# Executar container
docker run -d -p 8000:8000 --env-file .env fastapi-store
```

## 🔄 Metodologia TDD

Este projeto segue a metodologia **Test-Driven Development**:

1. **🔴 Red**: Escrever um teste que falha
2. **🟢 Green**: Implementar código mínimo para o teste passar
3. **🔵 Refactor**: Melhorar o código mantendo os testes

### Exemplo de fluxo TDD:
```bash
# 1. Escrever teste
pytest tests/test_product.py::test_create_product -v

# 2. Implementar funcionalidade
# Editar store/usecases/product.py

# 3. Executar teste novamente
pytest tests/test_product.py::test_create_product -v

# 4. Refatorar se necessário
```

## 📊 Endpoints Principais

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Health check da API |
| GET | `/products` | Listar todos os produtos |
| POST | `/products` | Criar novo produto |
| GET | `/products/{id}` | Buscar produto por ID |
| PUT | `/products/{id}` | Atualizar produto |
| DELETE | `/products/{id}` | Deletar produto |

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Scripts Úteis

```bash
# Instalar dependências
make install

# Executar aplicação
make run

# Executar testes
make test

# Executar linting
make lint

# Formatar código
make format
```

## 🐛 Solução de Problemas

### Erro de DATABASE_URL
```bash
# Verifique se o arquivo .env existe e tem a DATABASE_URL
cat .env

# Ou defina manualmente
export DATABASE_URL="mongodb://localhost:27017/store"
```

### MongoDB não conecta
```bash
# Verifique se o MongoDB está rodando
mongosh

# Ou inicie com Docker
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

## 👥 Autor

**Levi Costa**
- GitHub: [@LeviCostaSouza](https://github.com/LeviCostaSouza)
- LinkedIn: [Levi Costa](https://www.linkedin.com/in/levicostta)

## 🎓 Agradecimentos

- [Digital Innovation One (DIO)](https://digitalinnovation.one/) - Pelo bootcamp e projeto base
- [FastAPI](https://fastapi.tiangolo.com/) - Framework incrível
- Comunidade Python - Por todo suporte e documentação

---

⭐ **Se este projeto te ajudou, deixe uma estrela!** ⭐