.PHONY: up down build logs seed ingest test lint migrate ollama-check

up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build

logs:
	docker compose logs -f

seed:
	docker compose exec api python -m seed.runner

ingest:
	docker compose exec api python -m seed.ingest_knowledge

test:
	docker compose exec api pytest tests/ -v

test-unit:
	docker compose exec api pytest tests/unit/ -v

test-integration:
	docker compose exec api pytest tests/integration/ -v

test-e2e:
	docker compose exec api pytest tests/e2e/ -v

lint:
	docker compose exec api ruff check app/

migrate:
	docker compose exec api alembic upgrade head

migrate-new:
	docker compose exec api alembic revision --autogenerate -m "$(msg)"

shell-api:
	docker compose exec api bash

shell-db:
	docker compose exec db psql -U chefdecuisine

debug:
	docker compose --profile debug up -d

ollama-check:
	@echo "Checking Ollama connectivity..."
	@curl -sf http://localhost:11434/api/tags && echo "\nOllama is reachable" || echo "Ollama is NOT reachable at localhost:11434"
