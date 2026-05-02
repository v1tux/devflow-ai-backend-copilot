# DevFlow AI — AI Backend Copilot

DevFlow AI é uma plataforma para análise automatizada de repositórios, focada em qualidade de código, segurança, arquitetura, complexidade e boas práticas de engenharia.

O objetivo do projeto é demonstrar domínio profissional em Backend, APIs REST, FastAPI, React, PostgreSQL, Docker, CI/CD e análise estática de código.

## Visão do produto

O usuário conecta um repositório público do GitHub ou envia um projeto `.zip`. O sistema analisa os arquivos, calcula um score técnico e gera recomendações acionáveis para evolução do projeto.

## Funcionalidades

- Análise por URL pública do GitHub
- Upload de projeto `.zip`
- Score de qualidade de 0 a 100
- Detecção de code smells
- Detecção de complexidade ciclomática em Python
- Scanner de segurança com Bandit
- Validação de boas práticas de documentação e DevOps
- Histórico de análises
- Exportação de relatório em PDF
- API REST documentada com Swagger
- Frontend responsivo em React
- Ambiente completo com Docker Compose
- Pipeline CI com GitHub Actions

## Stack técnica

### Backend
- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- GitPython
- Radon
- Bandit
- ReportLab

### Frontend
- React
- Vite
- Axios
- Lucide React
- CSS responsivo

### Infraestrutura
- Docker
- Docker Compose
- GitHub Actions

## Arquitetura

```txt
devflow-ai/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── utils/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── styles/
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml
└── .github/workflows/ci.yml
```

## Como rodar com Docker

Pré-requisitos:

- Docker instalado
- Docker Compose instalado
- Git instalado

Clone o projeto:

```bash
git clone https://github.com/SEU-USUARIO/devflow-ai.git
cd devflow-ai
```

Suba os containers:

```bash
docker compose up --build
```

Acesse:

- Frontend: `http://localhost:5173`
- Backend: `http://localhost:8000`
- Swagger: `http://localhost:8000/docs`

## Como rodar sem Docker

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

No Windows PowerShell:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

### Frontend

Em outro terminal:

```bash
cd frontend
npm install
npm run dev
```

## Endpoints principais

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/health` | Verifica status da API |
| POST | `/api/analyses/repository` | Analisa repositório GitHub |
| POST | `/api/analyses/upload` | Analisa projeto enviado como ZIP |
| GET | `/api/analyses` | Lista histórico |
| GET | `/api/analyses/{id}` | Busca análise por ID |
| GET | `/api/analyses/{id}/report` | Baixa relatório PDF |

## Exemplo de body

```json
{
  "repository_url": "https://github.com/usuario/repositorio"
}
```

## Decisões técnicas

- A análise roda no backend para proteger regras de negócio e permitir evolução futura com filas.
- O projeto já possui separação em camadas: API, services, schemas, models, core e utils.
- O score é calculado por severidade dos achados técnicos.
- A IA possui fallback local para o sistema funcionar sem chave externa.
- O Docker Compose permite rodar frontend, backend e banco com um único comando.

## Roadmap profissional

- Autenticação com GitHub OAuth
- Multiusuário
- Planos SaaS
- Fila assíncrona com Celery + Redis
- Integração com OpenAI API para recomendações avançadas
- Comparação entre branches
- Comentários automáticos em Pull Requests
- Deploy em AWS ou Render
- Observabilidade com Prometheus e Grafana

## Autor

Victor Lobo Prates  
Software Engineer | Backend | Full Stack | APIs | Python | JavaScript
