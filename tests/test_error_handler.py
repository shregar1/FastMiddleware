"""
Tests for Error Handler middleware.
"""

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from src import ErrorHandlerMiddleware, ErrorConfig


class TestErrorHandlerMiddleware:
    """Tests for ErrorHandlerMiddleware."""
    
    @pytest.fixture
    def error_app(self) -> FastAPI:
        """Create app with error handler middleware."""
        app = FastAPI()
        app.add_middleware(
            ErrorHandlerMiddleware,
            include_exception_type=True,
        )
        
        @app.get("/error")
        async def raise_error():
            raise ValueError("Test error message")
        
        @app.get("/success")
        async def success():
            return {"status": "ok"}
        
        return app
    
    @pytest.fixture
    def error_client(self, error_app: FastAPI) -> TestClient:
        """Create test client for error app."""
        return TestClient(error_app, raise_server_exceptions=False)
    
    def test_catches_exception(self, error_client: TestClient):
        """Test that exceptions are caught and handled."""
        response = error_client.get("/error")
        
        assert response.status_code == 500
        data = response.json()
        assert data["error"] is True
        assert data["type"] == "ValueError"
    
    def test_success_passes_through(self, error_client: TestClient):
        """Test that successful requests pass through."""
        response = error_client.get("/success")
        
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


class TestErrorConfig:
    """Tests for ErrorConfig."""
    
    def test_default_config(self):
        """Test default configuration values."""
        config = ErrorConfig()
        
        assert config.include_traceback is False
        assert config.include_exception_type is False
        assert config.log_exceptions is True
        assert config.status_code == 500
    
    def test_custom_error_handlers(self):
        """Test custom error handlers."""
        config = ErrorConfig()
        config.error_handlers[ValueError] = (400, "Invalid value")
        config.error_handlers[PermissionError] = (403, "Permission denied")
        
        assert config.error_handlers[ValueError] == (400, "Invalid value")
        assert config.error_handlers[PermissionError] == (403, "Permission denied")


class TestTraceback:
    """Tests for traceback inclusion."""
    
    @pytest.fixture
    def traceback_app(self) -> FastAPI:
        """Create app with traceback enabled."""
        app = FastAPI()
        app.add_middleware(
            ErrorHandlerMiddleware,
            include_traceback=True,
            include_exception_type=True,
        )
        
        @app.get("/error")
        async def raise_error():
            raise RuntimeError("Detailed error")
        
        return app
    
    @pytest.fixture
    def traceback_client(self, traceback_app: FastAPI) -> TestClient:
        """Create test client for traceback app."""
        return TestClient(traceback_app, raise_server_exceptions=False)
    
    def test_includes_traceback(self, traceback_client: TestClient):
        """Test that traceback is included when configured."""
        response = traceback_client.get("/error")
        
        assert response.status_code == 500
        data = response.json()
        assert "traceback" in data
        assert isinstance(data["traceback"], list)

