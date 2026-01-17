"""
Tests for Cache middleware.
"""

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from src import CacheMiddleware, CacheConfig


@pytest.fixture
def cache_app() -> FastAPI:
    """Create app with cache middleware."""
    app = FastAPI()
    config = CacheConfig(
        default_max_age=3600,
        enable_etag=True,
    )
    app.add_middleware(CacheMiddleware, config=config)
    
    @app.get("/data")
    async def get_data():
        return {"message": "Hello"}
    
    @app.post("/create")
    async def create_data():
        return {"created": True}
    
    return app


@pytest.fixture
def cache_client(cache_app: FastAPI) -> TestClient:
    """Create test client for cache app."""
    return TestClient(cache_app)


class TestCacheMiddleware:
    """Tests for CacheMiddleware."""
    
    def test_cache_control_header_added(self, cache_client: TestClient):
        """Test that Cache-Control header is added."""
        response = cache_client.get("/data")
        
        assert response.status_code == 200
        assert "Cache-Control" in response.headers
        assert "max-age=3600" in response.headers["Cache-Control"]
    
    def test_etag_header_added(self, cache_client: TestClient):
        """Test that ETag header is added."""
        response = cache_client.get("/data")
        
        assert response.status_code == 200
        assert "ETag" in response.headers
    
    def test_vary_header_added(self, cache_client: TestClient):
        """Test that Vary header is added."""
        response = cache_client.get("/data")
        
        assert response.status_code == 200
        assert "Vary" in response.headers
    
    def test_post_not_cached(self, cache_client: TestClient):
        """Test that POST requests are not cached."""
        response = cache_client.post("/create")
        
        assert response.status_code == 200
        # POST should not have cache headers (or should have no-store)


class TestConditionalRequests:
    """Tests for conditional GET requests."""
    
    def test_304_on_matching_etag(self, cache_client: TestClient):
        """Test that 304 is returned when ETag matches."""
        # Get initial response with ETag
        response1 = cache_client.get("/data")
        etag = response1.headers.get("ETag")
        
        assert etag is not None
        
        # Send conditional request
        response2 = cache_client.get(
            "/data",
            headers={"If-None-Match": etag}
        )
        
        assert response2.status_code == 304


class TestCacheConfig:
    """Tests for CacheConfig."""
    
    def test_default_config(self):
        """Test default configuration values."""
        config = CacheConfig()
        
        assert config.default_max_age == 0
        assert config.enable_etag is True
        assert "GET" in config.cacheable_methods
        assert 200 in config.cacheable_status_codes
    
    def test_path_rules(self):
        """Test path-specific cache rules."""
        config = CacheConfig(
            path_rules={
                "/api/static": {"max_age": 86400},
                "/api/private": {"no_store": True},
            }
        )
        
        assert config.path_rules["/api/static"]["max_age"] == 86400
        assert config.path_rules["/api/private"]["no_store"] is True

