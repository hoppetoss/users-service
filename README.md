# FastAPI Template Service

A production-ready FastAPI template following the Golden Path best practices.

## Features

✅ **FastAPI** - Modern, fast web framework for building APIs
✅ **Type hints** - Full type safety with Python 3.12+
✅ **pytest** - Comprehensive test suite with TestClient
✅ **Black + Ruff** - Auto-formatting and linting
✅ **pre-commit** - Automatic code quality checks
✅ **Docker** - Production-ready containerization
✅ **Health checks** - Kubernetes-ready liveness and readiness probes

## Quick Start

\`\`\`bash
# Install dependencies
make dev

# Run tests
make test

# Start development server
make run

# Visit http://localhost:8000/docs for API documentation
\`\`\`

## Available Commands

| Command | Description |
|---------|-------------|
| \`make dev\` | Install with dev and test dependencies |
| \`make test\` | Run all tests |
| \`make coverage\` | Run tests with coverage report |
| \`make fmt\` | Format code with Black and Ruff |
| \`make lint\` | Check code quality |
| \`make run\` | Start development server |
| \`make hooks\` | Install pre-commit hooks |
| \`make clean\` | Remove virtual environment and cache files |

## Project Structure

\`\`\`
template-fastapi-service/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   └── tests/
│       ├── __init__.py
│       └── test_basic.py    # Test suite
├── .dockerignore
├── .gitignore
├── .pre-commit-config.yaml
├── Dockerfile
├── Makefile
├── pyproject.toml           # Project configuration
└── README.md
\`\`\`

## Health Endpoints

- \`GET /healthz\` - Liveness probe (is the app running?)
- \`GET /readyz\` - Readiness probe (can it serve traffic?)
- \`GET /docs\` - Interactive API documentation (Swagger UI)
- \`GET /redoc\` - Alternative API documentation (ReDoc)

## Testing

\`\`\`bash
# Run all tests
make test

# Run with coverage
make coverage

# Run specific test
pytest app/tests/test_basic.py::test_healthz -v
\`\`\`

## Docker

\`\`\`bash
# Build image
docker build -t template-fastapi-service .

# Run container
docker run -p 8000:8000 template-fastapi-service

# Test health endpoint
curl http://localhost:8000/healthz
\`\`\`

## Next Steps

1. Add your business logic to \`app/\`
2. Create new endpoint modules as needed
3. Add integration tests
4. Configure CI/CD (see Phase 2 of the Golden Path)
5. Add observability (see Phase 3 of the Golden Path)
