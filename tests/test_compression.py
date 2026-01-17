"""
Tests for Compression middleware.
"""

import gzip
import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from src import CompressionMiddleware, CompressionConfig


@pytest.fixture
def compression_app(sample_routes) -> FastAPI:
    """Create app with compression middleware."""
    app = sample_routes
    app.add_middleware(CompressionMiddleware)
    return app


@pytest.fixture
def compression_client(compression_app: FastAPI) -> TestClient:
    """Create test client for compression app."""
    return TestClient(compression_app)


class TestCompressionMiddleware:
    """Tests for CompressionMiddleware."""
    
    def test_compresses_when_accepted(self, compression_client: TestClient):
        """Test that response is compressed when client accepts gzip."""
        response = compression_client.get(
            "/",
            headers={"Accept-Encoding": "gzip, deflate"}
        )
        
        assert response.status_code == 200
        assert response.headers.get("Vary") == "Accept-Encoding"
    
    def test_no_compression_without_accept_header(self, compression_client: TestClient):
        """Test no compression when client doesn't accept gzip."""
        response = compression_client.get("/")
        
        assert response.status_code == 200
        assert "Content-Encoding" not in response.headers


class TestCompressionConfig:
    """Tests for CompressionConfig."""
    
    def test_default_config(self):
        """Test default configuration values."""
        config = CompressionConfig()
        
        assert config.minimum_size == 500
        assert config.compression_level == 6
        assert "application/json" in config.compressible_types
    
    def test_custom_config(self):
        """Test custom configuration values."""
        config = CompressionConfig(
            minimum_size=1000,
            compression_level=9,
        )
        
        assert config.minimum_size == 1000
        assert config.compression_level == 9

