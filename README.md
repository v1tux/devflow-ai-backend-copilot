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

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT / OAuth2
- Passlib
- Pydantic Settings
- Docker

### Frontend

- React
- Vite
- TypeScript

### DevOps

- Docker Compose
- GitHub Actions
- Ruff Lint

---

## 📂 Project Architecture

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
🔐 Authentication

The API uses JWT-based authentication.

Authentication flow:

The user creates an account using POST /auth/register.
The user logs in using POST /auth/login or the Swagger Authorize button.
The API generates a JWT access token.
Protected routes require the token in the request header.
Requests without a valid token return 401 Unauthorized.

Protected routes:

POST /analyses/repository
POST /analyses/upload
GET  /analyses
GET  /analyses/{analysis_id}
GET  /analyses/{analysis_id}/report

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

Frontend:

http://127.0.0.1:5173

Swagger documentation:

http://127.0.0.1:8000/docs

Backend API:

http://127.0.0.1:8000

⚙️ Environment Variables

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

🧪 CI/CD

The project includes a GitHub Actions pipeline with:

Backend lint validation with Ruff
Frontend build validation
Basic project validation for continuous integration

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

👨‍💻 Author

Victor Anderson Lobo Prates

GitHub:
https://github.com/v1tux

LinkedIn:
https://linkedin.com/in/victor-lobo-prates-196970233

⭐ About this project

This project is part of a backend engineering portfolio focused on demonstrating practical skills with API development, authentication, database persistence, Docker, CI/CD and software quality analysis.
