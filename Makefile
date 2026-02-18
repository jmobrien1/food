.PHONY: up down build logs seed test lint migrate

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
