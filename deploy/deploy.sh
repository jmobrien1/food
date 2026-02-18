#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "=== Chef de Cuisine — Deploy ==="

# Pre-flight checks
if ! command -v docker &> /dev/null; then
    echo "ERROR: docker not found"
    exit 1
fi

if ! docker compose version &> /dev/null; then
    echo "ERROR: docker compose not found"
    exit 1
fi

if [ ! -f .env ]; then
    echo "WARNING: .env not found — copying from .env.example"
    cp .env.example .env
    echo "Edit .env before first use"
fi

# Check Ollama connectivity (non-blocking warning)
if curl -sf http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "Ollama is reachable"
else
    echo "WARNING: Ollama not reachable at localhost:11434 — local LLM will fail"
fi

# Pull latest if this is a git repo
if [ -d .git ]; then
    echo "Pulling latest code..."
    git pull --ff-only
fi

# Build and start
echo "Building containers..."
docker compose build api

echo "Starting services..."
docker compose up -d

# Health check
echo "Waiting for API health..."
for i in $(seq 1 30); do
    if curl -sf http://localhost:8004/api/v1/health > /dev/null 2>&1; then
        echo "API is healthy!"
        break
    fi
    if [ "$i" -eq 30 ]; then
        echo "ERROR: API failed to become healthy after 150s"
        docker compose logs api --tail 30
        exit 1
    fi
    echo "  Attempt $i/30..."
    sleep 5
done

# Cleanup
docker image prune -f

echo ""
echo "=== Deploy complete ==="
docker compose ps
echo ""
echo "Frontend: http://10.0.0.5:3004"
echo "API:      http://10.0.0.5:8004"
echo "API Docs: http://10.0.0.5:8004/docs"
