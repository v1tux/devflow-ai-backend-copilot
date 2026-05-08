🚀 DevFlow AI

<img width="1269" height="617" alt="DevFlow" src="https://github.com/user-attachments/assets/64de87eb-6f7e-4c75-9fc4-99ec1b8d7bce" />

Plataforma inteligente para análise de repositórios, detecção de code smells, riscos de segurança, problemas arquiteturais e geração de score técnico profissional.

---

✨ Features

- 🔐 JWT Authentication (OAuth2)
- 🛡️ Rotas protegidas
- 🐘 PostgreSQL persistence
- 🐳 Dockerized environment
- ⚡ FastAPI backend
- 📊 Code quality analysis
- 📄 PDF report generation
- 👥 Multi-user architecture
- 📈 Metrics endpoint
- ❤️ Healthcheck endpoint
- 🔍 Repository & ZIP analysis

---

🧠 Tech Stack

Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT / OAuth2
- Passlib
- Docker

Frontend

- React
- Vite
- TypeScript

DevOps

- Docker Compose
- GitHub Actions
- Ruff Lint

---

📂 Architecture

backend/
 ├── app/
 │   ├── api/
 │   ├── auth/
 │   ├── core/
 │   ├── models/
 │   ├── schemas/
 │   ├── services/
 │   └── utils/
frontend/

---

🔐 Authentication Flow

- User registration
- JWT token generation
- Protected routes
- User-scoped analyses

---

📊 API Endpoints

Auth

POST /auth/register
POST /auth/login
POST /auth/token

Analyses

POST /analyses/repository
POST /analyses/upload
GET  /analyses
GET  /analyses/{id}
GET  /analyses/{id}/report

System

GET /health
GET /metrics

---

🐳 Running Locally

Docker

docker compose up --build

Frontend:

http://127.0.0.1:5173

Swagger:

http://127.0.0.1:8000/docs

---

📈 Roadmap

- [x] JWT Authentication
- [x] PostgreSQL persistence
- [x] Docker environment
- [x] Multi-user support
- [x] Metrics endpoint
- [ ] Frontend authentication
- [ ] User dashboard
- [ ] Deploy production
- [ ] AI-powered advanced analysis
- [ ] Background queue processing

---

🧪 CI/CD

GitHub Actions pipeline with:

- Ruff lint
- Frontend validation
- Backend validation

---

👨‍💻 Author

Victor Anderson Lobo Prates

🔗 GitHub:
https://github.com/v1tux

🔗 LinkedIn:
https://linkedin.com/in/victor-lobo-prates-196970233

---

⭐ Vision

DevFlow AI aims to become a complete developer intelligence platform capable of evaluating architecture, security, maintainability and engineering quality of software projects.
