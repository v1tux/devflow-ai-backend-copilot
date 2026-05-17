# 🚀 DevFlow AI

<img width="1269" height="617" alt="DevFlow" src="https://github.com/user-attachments/assets/64de87eb-6f7e-4c75-9fc4-99ec1b8d7bce" />

O **DevFlow AI** é uma plataforma inteligente para análise de repositórios de software, identificação de *code smells*, riscos de segurança, problemas arquiteturais, pontos de melhoria e geração de um score técnico do projeto.

O objetivo do projeto é simular uma aplicação real de Back-End, aplicando boas práticas como autenticação JWT, rotas protegidas, persistência com PostgreSQL, ambiente Dockerizado, organização em camadas e validação automatizada com CI/CD.

---

## ✨ Funcionalidades

- 🔐 Autenticação com JWT e OAuth2
- 🛡️ Rotas de análise protegidas
- 🐘 Persistência com PostgreSQL
- 🐳 Ambiente Dockerizado com Docker Compose
- ⚡ API Back-End com FastAPI
- 📊 Análise de qualidade de código
- 🔍 Análise de repositórios GitHub
- 📦 Upload e análise de projetos em `.zip`
- 📄 Geração de relatório em PDF
- ❤️ Endpoint de healthcheck
- 📈 Endpoint de métricas
- ⚙️ Configuração por variáveis de ambiente
- 🧪 Pipeline CI com validação de lint e build

---

## 🧠 Stack Técnica

### Back-End

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT / OAuth2
- Passlib
- Pydantic Settings
- Docker

### Front-End

- React
- Vite
- TypeScript

### DevOps / Qualidade

- Docker Compose
- GitHub Actions
- Ruff Lint

---

## 📂 Arquitetura do Projeto

```txt
devflow-ai/
├── backend/
│   └── app/
│       ├── api/
│       ├── auth/
│       ├── core/
│       ├── models/
│       ├── schemas/
│       ├── services/
│       └── utils/
│
├── frontend/
│   └── src/
│
├── docker-compose.yml
└── README.md
```

The API uses JWT-based authentication.

## 🔐 Autenticação

A API utiliza autenticação baseada em **JWT**.

Fluxo básico:

1. O usuário cria uma conta em `POST /auth/register`.
2. O usuário realiza login em `POST /auth/login` ou pelo botão `Authorize` do Swagger.
3. A API gera um token JWT.
4. As rotas protegidas exigem o token no cabeçalho da requisição.
5. Requisições sem token válido retornam `401 Unauthorized`.

Rotas protegidas:

```txt
POST /analyses/repository
POST /analyses/upload
GET  /analyses
GET  /analyses/{analysis_id}
GET  /analyses/{analysis_id}/report
```

Formato do cabeçalho de autorização:

```txt
Authorization: Bearer <access_token>
```

---

## 📊 Endpoints da API

### Autenticação

```txt
POST /auth/register
POST /auth/login
POST /auth/token
```

### Análises

```txt
POST /analyses/repository
POST /analyses/upload
GET  /analyses
GET  /analyses/{analysis_id}
GET  /analyses/{analysis_id}/report
```

### Sistema

```txt
GET /health
GET /metrics
```

---

## 🐳 Como Executar Localmente

### Requisitos

- Docker
- Docker Compose

### Subir o projeto

```bash
docker compose up --build
```

### Acessos

Front-End:

```txt
http://127.0.0.1:5173
```

Swagger documentation:

```txt
http://127.0.0.1:8000/docs
```

API Back-End:

```txt
http://127.0.0.1:8000
```

Backend API:

## ⚙️ Variáveis de Ambiente

O Back-End utiliza variáveis de ambiente para configuração.

Crie um arquivo `.env` dentro da pasta `backend/` com base no arquivo `.env.example`.

Exemplo:

```env
APP_NAME=DevFlow AI
APP_ENV=development
SECRET_KEY=your-local-secret-key
DATABASE_URL=postgresql+psycopg://postgres:postgres@db:5432/devflow
OPENAI_API_KEY=
CORS_ORIGINS=http://localhost:5173
```

O arquivo `.env` não deve ser enviado para o GitHub.

The backend uses environment variables for configuration.

Create a .env file inside the backend/ folder based on .env.example.

Example:

APP_NAME=DevFlow AI
APP_ENV=development
SECRET_KEY=your-local-secret-key
DATABASE_URL=postgresql+psycopg://postgres:postgres@db:5432/devflow
OPENAI_API_KEY=
CORS_ORIGINS=http://localhost:5173

The .env file should not be committed to GitHub.

## 🧪 CI/CD

O projeto possui pipeline com GitHub Actions contendo:

- Validação de lint do Back-End com Ruff
- Validação de build do Front-End
- Verificação básica da integridade do projeto

Melhorias planejadas para o CI/CD:

- Executar testes automatizados com Pytest
- Adicionar relatório de cobertura de testes
- Adicionar validações de segurança no pipeline


## 📈 Roadmap

### Concluído

- [x] API com FastAPI
- [x] Persistência com PostgreSQL
- [x] Ambiente com Docker Compose
- [x] Configuração por variáveis de ambiente
- [x] Autenticação com JWT
- [x] Fluxo OAuth2 integrado ao Swagger
- [x] Rotas de análise protegidas
- [x] Análise de repositórios GitHub
- [x] Upload e análise de projetos `.zip`
- [x] Geração de relatório em PDF
- [x] Endpoint de healthcheck
- [x] Endpoint de métricas
- [x] Pipeline com GitHub Actions

### Próximos Passos

- [ ] Vincular cada análise ao usuário autenticado
- [ ] Filtrar histórico de análises pelo usuário logado
- [ ] Impedir acesso a relatórios de outros usuários
- [ ] Adicionar migrations com Alembic
- [ ] Executar testes automatizados no CI
- [ ] Melhorar o fluxo de autenticação no Front-End
- [ ] Criar dashboard do usuário
- [ ] Adicionar paginação na listagem de análises
- [ ] Implementar fila em background para análises longas
- [ ] Preparar deploy em ambiente de produção

### Melhorias Futuras

- [ ] Análise avançada com IA
- [ ] Comparação entre diferentes análises do mesmo repositório
- [ ] Score separado por segurança
- [ ] Score separado por arquitetura
- [ ] Histórico de evolução da qualidade do projeto
- [ ] Suporte a times ou workspaces
- [ ] Observabilidade com logs e métricas em produção

---

## 🧭 Visão do Produto

O **DevFlow AI** tem como objetivo se tornar uma plataforma de inteligência para desenvolvedores, capaz de avaliar projetos de software por diferentes perspectivas técnicas:

- Arquitetura
- Segurança
- Manutenibilidade
- Qualidade de código
- Experiência de desenvolvimento
- Maturidade de engenharia

A proposta é ajudar desenvolvedores, times e avaliadores técnicos a entender rapidamente a saúde de um projeto e identificar melhorias de maior impacto.

---

## 👨‍💻 Autor

**Victor Anderson Lobo Prates**

GitHub:  
https://github.com/v1tux

LinkedIn:  
https://linkedin.com/in/victor-lobo-prates-196970233

⭐ About this project

## ⭐ Sobre este projeto

Este projeto faz parte de um portfólio focado em Back-End, com o objetivo de demonstrar habilidades práticas em desenvolvimento de APIs, autenticação, banco de dados, Docker, CI/CD e análise de qualidade de software.
