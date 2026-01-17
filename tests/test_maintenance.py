"""
Tests for Maintenance Mode middleware.
"""

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from src import MaintenanceMiddleware, MaintenanceConfig


class TestMaintenanceModeDisabled:
    """Tests for maintenance mode when disabled."""
    
    @pytest.fixture
    def disabled_app(self) -> FastAPI:
        """Create app with maintenance mode disabled."""
        app = FastAPI()
        app.add_middleware(
            MaintenanceMiddleware,
            enabled=False,
        )
        
        @app.get("/")
        async def root():
            return {"message": "Hello"}
        
        return app
    
    @pytest.fixture
    def disabled_client(self, disabled_app: FastAPI) -> TestClient:
        """Create test client for disabled maintenance app."""
        return TestClient(disabled_app)
    
    def test_requests_pass_through(self, disabled_client: TestClient):
        """Test that requests pass through when disabled."""
        response = disabled_client.get("/")
        
        assert response.status_code == 200
        assert response.json() == {"message": "Hello"}


class TestMaintenanceModeEnabled:
    """Tests for maintenance mode when enabled."""
    
    @pytest.fixture
    def enabled_app(self) -> FastAPI:
        """Create app with maintenance mode enabled."""
        app = FastAPI()
        config = MaintenanceConfig(
            enabled=True,
            message="Under maintenance",
            retry_after=300,
        )
        app.add_middleware(MaintenanceMiddleware, config=config)
        
        @app.get("/")
        async def root():
            return {"message": "Hello"}
        
        @app.get("/health")
        async def health():
            return {"status": "ok"}
        
        return app
    
    @pytest.fixture
    def enabled_client(self, enabled_app: FastAPI) -> TestClient:
        """Create test client for enabled maintenance app."""
        return TestClient(enabled_app)
    
    def test_returns_503(self, enabled_client: TestClient):
        """Test that 503 is returned during maintenance."""
        response = enabled_client.get("/")
        
        assert response.status_code == 503
        data = response.json()
        assert data["maintenance"] is True
        assert data["message"] == "Under maintenance"
    
    def test_retry_after_header(self, enabled_client: TestClient):
        """Test that Retry-After header is set."""
        response = enabled_client.get("/")
        
        assert response.headers.get("Retry-After") == "300"
        assert response.headers.get("X-Maintenance-Mode") == "true"


class TestMaintenanceBypass:
    """Tests for maintenance mode bypass."""
    
    @pytest.fixture
    def bypass_app(self) -> FastAPI:
        """Create app with bypass options."""
        app = FastAPI()
        config = MaintenanceConfig(
            enabled=True,
            allowed_paths={"/health"},
            allowed_ips={"127.0.0.1"},
            bypass_token="secret-token",
        )
        app.add_middleware(MaintenanceMiddleware, config=config)
        
        @app.get("/")
        async def root():
            return {"message": "Hello"}
        
        @app.get("/health")
        async def health():
            return {"status": "ok"}
        
        return app
    
    @pytest.fixture
    def bypass_client(self, bypass_app: FastAPI) -> TestClient:
        """Create test client for bypass app."""
        return TestClient(bypass_app)
    
    def test_allowed_path_bypasses(self, bypass_client: TestClient):
        """Test that allowed paths bypass maintenance."""
        response = bypass_client.get("/health")
        
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
    
    def test_bypass_token_works(self, bypass_client: TestClient):
        """Test that bypass token allows access."""
        response = bypass_client.get(
            "/",
            headers={"X-Maintenance-Bypass": "secret-token"}
        )
        
        assert response.status_code == 200


class TestMaintenanceConfig:
    """Tests for MaintenanceConfig."""
    
    def test_default_config(self):
        """Test default configuration values."""
        config = MaintenanceConfig()
        
        assert config.enabled is False
        assert config.retry_after == 300
        assert config.bypass_header == "X-Maintenance-Bypass"
    
    def test_custom_config(self):
        """Test custom configuration values."""
        config = MaintenanceConfig(
            enabled=True,
            message="Custom message",
            retry_after=600,
        )
        
        assert config.enabled is True
        assert config.message == "Custom message"
        assert config.retry_after == 600


class TestDynamicToggle:
    """Tests for dynamically enabling/disabling maintenance."""
    
    def test_enable_disable(self):
        """Test enabling and disabling maintenance at runtime."""
        app = FastAPI()
        
        config = MaintenanceConfig(enabled=False)
        middleware = MaintenanceMiddleware(app, config=config)
        
        assert middleware.is_enabled() is False
        
        middleware.enable(message="Going down for maintenance")
        assert middleware.is_enabled() is True
        
        middleware.disable()
        assert middleware.is_enabled() is False

