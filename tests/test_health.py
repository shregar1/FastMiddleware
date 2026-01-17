"""
Tests for Health Check middleware.
"""

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from src import HealthCheckMiddleware, HealthConfig


@pytest.fixture
def health_app() -> FastAPI:
    """Create app with health check middleware."""
    app = FastAPI()
    config = HealthConfig(
        version="1.0.0",
        service_name="test-service",
    )
    app.add_middleware(HealthCheckMiddleware, config=config)
    
    @app.get("/")
    async def root():
        return {"message": "Hello"}
    
    return app


@pytest.fixture
def health_client(health_app: FastAPI) -> TestClient:
    """Create test client for health app."""
    return TestClient(health_app)


class TestHealthCheckMiddleware:
    """Tests for HealthCheckMiddleware."""
    
    def test_health_endpoint(self, health_client: TestClient):
        """Test that /health endpoint returns health status."""
        response = health_client.get("/health")
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
        assert "uptime_seconds" in data
        assert data["version"] == "1.0.0"
        assert data["service"] == "test-service"
    
    def test_ready_endpoint(self, health_client: TestClient):
        """Test that /ready endpoint returns readiness status."""
        response = health_client.get("/ready")
        
        assert response.status_code == 200
        data = response.json()
        assert data["ready"] is True
        assert "timestamp" in data
    
    def test_live_endpoint(self, health_client: TestClient):
        """Test that /live endpoint returns liveness status."""
        response = health_client.get("/live")
        
        assert response.status_code == 200
        data = response.json()
        assert data["alive"] is True
    
    def test_other_routes_pass_through(self, health_client: TestClient):
        """Test that other routes pass through to app."""
        response = health_client.get("/")
        
        assert response.status_code == 200
        assert response.json() == {"message": "Hello"}


class TestHealthConfig:
    """Tests for HealthConfig."""
    
    def test_default_paths(self):
        """Test default health check paths."""
        config = HealthConfig()
        
        assert config.health_path == "/health"
        assert config.ready_path == "/ready"
        assert config.live_path == "/live"
    
    def test_custom_paths(self):
        """Test custom health check paths."""
        config = HealthConfig(
            health_path="/healthz",
            ready_path="/readiness",
            live_path="/liveness",
        )
        
        assert config.health_path == "/healthz"
        assert config.ready_path == "/readiness"
        assert config.live_path == "/liveness"


class TestCustomHealthChecks:
    """Tests for custom health check functions."""
    
    @pytest.fixture
    def custom_check_app(self) -> FastAPI:
        """Create app with custom health checks."""
        app = FastAPI()
        
        async def check_database():
            return True
        
        async def check_cache():
            return False  # Simulating unhealthy cache
        
        config = HealthConfig(
            custom_checks={
                "database": check_database,
                "cache": check_cache,
            }
        )
        app.add_middleware(HealthCheckMiddleware, config=config)
        
        return app
    
    @pytest.fixture
    def custom_check_client(self, custom_check_app: FastAPI) -> TestClient:
        """Create test client for custom check app."""
        return TestClient(custom_check_app)
    
    def test_custom_checks_included(self, custom_check_client: TestClient):
        """Test that custom checks are included in response."""
        response = custom_check_client.get("/health")
        
        assert response.status_code == 503  # Unhealthy due to cache
        data = response.json()
        assert data["status"] == "unhealthy"
        assert data["checks"]["database"] == "healthy"
        assert data["checks"]["cache"] == "unhealthy"

