<<<<<<< HEAD
 🚀 DevFlow AI

<img width="1269" height="617" alt="DevFlow" src="https://github.com/user-attachments/assets/64de87eb-6f7e-4c75-9fc4-99ec1b8d7bce" />

DevFlow AI is an intelligent platform for analyzing software repositories, identifying code smells, security risks, architectural issues, maintainability problems and generating a technical quality score with actionable recommendations.

The project was built as a backend-focused portfolio application, simulating real-world engineering practices such as authentication, protected API routes, Dockerized services, database persistence and automated validation.

---

## ✨ Features

- 🔐 JWT authentication with OAuth2 Password Bearer flow
- 🛡️ Protected analysis routes
- 🐘 PostgreSQL persistence
- 🐳 Dockerized development environment
- ⚡ FastAPI backend
- 📊 Code quality analysis
- 🔍 GitHub repository analysis
- 📦 ZIP project upload analysis
- 📄 PDF report generation
- ❤️ Healthcheck endpoint
- 📈 Metrics endpoint
- ⚙️ Environment-based configuration
- 🧪 CI pipeline with lint and build validation

---

## 🧠 Tech Stack

### Backend
=======
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
>>>>>>> 5ac8255 (docs: update README in Portugese)

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT / OAuth2
- Passlib
- Pydantic Settings
- Docker

<<<<<<< HEAD
### Frontend
=======
### Front-End
>>>>>>> 5ac8255 (docs: update README in Portugese)

- React
- Vite
- TypeScript

<<<<<<< HEAD
### DevOps
=======
### DevOps / Qualidade
>>>>>>> 5ac8255 (docs: update README in Portugese)

- Docker Compose
- GitHub Actions
- Ruff Lint

---

<<<<<<< HEAD
## 📂 Project Architecture
=======
## 📂 Arquitetura do Projeto
>>>>>>> 5ac8255 (docs: update README in Portugese)

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
<<<<<<< HEAD
🔐 Authentication
=======
```
>>>>>>> 5ac8255 (docs: update README in Portugese)

The API uses JWT-based authentication.

<<<<<<< HEAD
Authentication flow:

The user creates an account using POST /auth/register.
The user logs in using POST /auth/login or the Swagger Authorize button.
The API generates a JWT access token.
Protected routes require the token in the request header.
Requests without a valid token return 401 Unauthorized.

Protected routes:
=======
## 🔐 Autenticação

A API utiliza autenticação baseada em **JWT**.

Fluxo básico:

1. O usuário cria uma conta em `POST /auth/register`.
2. O usuário realiza login em `POST /auth/login` ou pelo botão `Authorize` do Swagger.
3. A API gera um token JWT.
4. As rotas protegidas exigem o token no cabeçalho da requisição.
5. Requisições sem token válido retornam `401 Unauthorized`.

Rotas protegidas:
>>>>>>> 5ac8255 (docs: update README in Portugese)

```txt
POST /analyses/repository
POST /analyses/upload
GET  /analyses
GET  /analyses/{analysis_id}
GET  /analyses/{analysis_id}/report
<<<<<<< HEAD

Authorization header format:

Authorization: Bearer <access_token>

📊 API Endpoints
Auth
POST /auth/register
POST /auth/login
POST /auth/token
Analyses
POST /analyses/repository
POST /analyses/upload
GET  /analyses
GET  /analyses/{analysis_id}
GET  /analyses/{analysis_id}/report
System
GET /health
GET /metrics

🐳 Running Locally
Requirements
Docker
Docker Compose
Start the project
docker compose up --build
Access the application
=======
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
>>>>>>> 5ac8255 (docs: update README in Portugese)

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

<<<<<<< HEAD
http://127.0.0.1:8000

⚙️ Environment Variables
=======
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
>>>>>>> 5ac8255 (docs: update README in Portugese)

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

<<<<<<< HEAD
The project includes a GitHub Actions pipeline with:

Backend lint validation with Ruff
Frontend build validation
Basic project validation for continuous integration
=======
O projeto possui pipeline com GitHub Actions contendo:

- Validação de lint do Back-End com Ruff
- Validação de build do Front-End
- Verificação básica da integridade do projeto

Melhorias planejadas para o CI/CD:

- Executar testes automatizados com Pytest
- Adicionar relatório de cobertura de testes
- Adicionar validações de segurança no pipeline
>>>>>>> 5ac8255 (docs: update README in Portugese)

Planned CI improvements:

Run automated backend tests with Pytest
Add test coverage reports
Add security checks to the pipeline

📈 Roadmap

Completed
 FastAPI backend
 PostgreSQL persistence
 Docker Compose environment
 Environment-based configuration
 JWT authentication
 OAuth2 flow integrated with Swagger
 Protected analysis routes
 GitHub repository analysis
 ZIP upload analysis
 PDF report generation
 Healthcheck endpoint
 Metrics endpoint
 GitHub Actions CI pipeline

In Progress / Next Steps
 Link each analysis to the authenticated user
 Filter analysis history by logged-in user
 Prevent users from accessing reports from other users
 Add Alembic migrations
 Add automated Pytest execution to CI
 Improve frontend authentication flow
 Add user dashboard
 Add pagination to analysis listing
 Add background queue processing for long analyses
 Prepare production deployment

Future Improvements
 Advanced AI-powered analysis
 Repository comparison between different analysis runs
 Security score breakdown
 Architecture score breakdown
 Historical evolution of project quality
 Team/workspace support
 Production observability with logs and metrics
🧭 Product Vision

DevFlow AI aims to become a developer intelligence platform capable of evaluating software projects from multiple technical perspectives:

Architecture
Security
Maintainability
Code quality
Developer experience
Engineering maturity

The goal is to help developers, teams and technical reviewers quickly understand the health of a project and identify the highest-impact improvements.

## 📈 Roadmap

### Concluído

<<<<<<< HEAD
GitHub:
https://github.com/v1tux

LinkedIn:
=======
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
>>>>>>> 5ac8255 (docs: update README in Portugese)
https://linkedin.com/in/victor-lobo-prates-196970233

⭐ About this project

<<<<<<< HEAD
This project is part of a backend engineering portfolio focused on demonstrating practical skills with API development, authentication, database persistence, Docker, CI/CD and software quality analysis.
=======
## ⭐ Sobre este projeto

Este projeto faz parte de um portfólio focado em Back-End, com o objetivo de demonstrar habilidades práticas em desenvolvimento de APIs, autenticação, banco de dados, Docker, CI/CD e análise de qualidade de software.
>>>>>>> 5ac8255 (docs: update README in Portugese)
