.PHONY: help install fmt lint test run clean hooks coverage dev

help:
	@echo "Available commands:"
	@echo "  make install   - Install production dependencies"
	@echo "  make dev       - Install with dev and test dependencies"
	@echo "  make fmt       - Format code with Black and Ruff"
	@echo "  make lint      - Check code quality"
	@echo "  make test      - Run tests"
	@echo "  make coverage  - Run tests with coverage report"
	@echo "  make run       - Start the development server"
	@echo "  make hooks     - Install pre-commit hooks"
	@echo "  make clean     - Remove virtual environment and cache files"

install:
	python -m venv .venv && . .venv/bin/activate && pip install -e .

dev:
	python -m venv .venv && . .venv/bin/activate && pip install -e ".[dev,test]"

fmt:
	ruff check . --fix
	black .

lint:
	ruff check .
	black --check .

test:
	PYTHONPATH=. pytest

coverage:
	PYTHONPATH=. pytest --cov=app --cov-report=term-missing --cov-report=html

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

clean:
	rm -rf .venv __pycache__ .pytest_cache .coverage htmlcov
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

hooks:
	pre-commit install
	pre-commit run --all-files || true
