# Chef de Cuisine

AI-powered culinary assistant that translates Michelin-level techniques into constraint-aware, home-kitchen-friendly execution plans.

## Architecture

- **Backend**: FastAPI + SQLAlchemy + PostgreSQL/pgvector
- **Frontend**: Next.js + React + Tailwind CSS
- **AI**: Claude Sonnet 4.6 via Anthropic API
- **Pipeline**: 4-agent system (Audit → Translate → Schedule → Chef Secrets)

## Quick Start

```bash
cp .env.example .env
# Edit .env with your ANTHROPIC_API_KEY

docker compose up -d
```

- Frontend: http://localhost:3000
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Development

```bash
make up          # Start all services
make logs        # Tail logs
make test        # Run all tests
make test-unit   # Run unit tests
make shell-api   # Shell into API container
make shell-db    # psql into database
make debug       # Start with pgAdmin at :5050
```

## API Endpoints

```
POST /api/v1/plans/generate       — Generate execution plan
GET  /api/v1/plans/{id}           — Retrieve saved plan
GET  /api/v1/ingredients          — Search ingredients
GET  /api/v1/ingredients/{id}/affinities — Flavor affinities
POST /api/v1/substitutions/suggest — Suggest replacements
GET  /api/v1/health               — Health check
GET  /api/v1/health/ready         — Readiness check
```
