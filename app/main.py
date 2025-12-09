"""FastAPI Template Service - Golden Path Reference Implementation."""

from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Template Service",
    description="A production-ready FastAPI template following the Golden Path",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/healthz", tags=["Health"])
def healthz() -> dict[str, str]:
    """
    Liveness probe endpoint.

    Returns 200 if the application is running.
    Used by Kubernetes to know if the pod should be restarted.
    """
    return {"status": "ok"}


@app.get("/readyz", tags=["Health"])
def readyz() -> dict[str, str]:
    """
    Readiness probe endpoint.

    Returns 200 if the application is ready to serve traffic.
    Used by Kubernetes to know if the pod should receive requests.
    In production, add checks for database connections, cache, etc.
    """
    return {"status": "ready"}
