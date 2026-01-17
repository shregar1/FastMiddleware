"""
Tests for Idempotency middleware.
"""

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from src import IdempotencyMiddleware, IdempotencyConfig, InMemoryIdempotencyStore


@pytest.fixture
def idempotency_app() -> FastAPI:
    """Create app with idempotency middleware."""
    app = FastAPI()
    app.add_middleware(IdempotencyMiddleware)
    
    counter = {"value": 0}
    
    @app.post("/create")
    async def create():
        counter["value"] += 1
        return {"created": True, "count": counter["value"]}
    
    @app.get("/read")
    async def read():
        return {"count": counter["value"]}
    
    return app


@pytest.fixture
def idempotency_client(idempotency_app: FastAPI) -> TestClient:
    """Create test client for idempotency app."""
    return TestClient(idempotency_app)


class TestIdempotencyMiddleware:
    """Tests for IdempotencyMiddleware."""
    
    def test_request_with_key_is_cached(self, idempotency_client: TestClient):
        """Test that requests with idempotency key are cached."""
        key = "unique-key-123"
        
        # First request
        response1 = idempotency_client.post(
            "/create",
            headers={"Idempotency-Key": key}
        )
        assert response1.status_code == 200
        assert response1.json()["count"] == 1
        
        # Second request with same key (should return cached)
        response2 = idempotency_client.post(
            "/create",
            headers={"Idempotency-Key": key}
        )
        assert response2.status_code == 200
        assert response2.json()["count"] == 1  # Same as first request
        assert response2.headers.get("X-Idempotent-Replayed") == "true"
    
    def test_different_keys_not_cached(self, idempotency_client: TestClient):
        """Test that different keys produce different responses."""
        response1 = idempotency_client.post(
            "/create",
            headers={"Idempotency-Key": "key-1"}
        )
        response2 = idempotency_client.post(
            "/create",
            headers={"Idempotency-Key": "key-2"}
        )
        
        assert response1.json()["count"] != response2.json()["count"]
    
    def test_get_requests_not_affected(self, idempotency_client: TestClient):
        """Test that GET requests are not affected by idempotency."""
        response = idempotency_client.get("/read")
        assert response.status_code == 200
        assert "X-Idempotent-Replayed" not in response.headers


class TestIdempotencyConfig:
    """Tests for IdempotencyConfig."""
    
    def test_default_config(self):
        """Test default configuration values."""
        config = IdempotencyConfig()
        
        assert config.header_name == "Idempotency-Key"
        assert config.ttl_seconds == 86400
        assert "POST" in config.required_methods
        assert config.require_key is False
    
    def test_custom_config(self):
        """Test custom configuration values."""
        config = IdempotencyConfig(
            header_name="X-Idempotency-Key",
            ttl_seconds=3600,
            require_key=True,
        )
        
        assert config.header_name == "X-Idempotency-Key"
        assert config.ttl_seconds == 3600
        assert config.require_key is True


class TestRequiredKey:
    """Tests for required idempotency key."""
    
    @pytest.fixture
    def required_key_app(self) -> FastAPI:
        """Create app with required idempotency key."""
        app = FastAPI()
        config = IdempotencyConfig(require_key=True)
        app.add_middleware(IdempotencyMiddleware, config=config)
        
        @app.post("/create")
        async def create():
            return {"created": True}
        
        return app
    
    @pytest.fixture
    def required_key_client(self, required_key_app: FastAPI) -> TestClient:
        """Create test client for required key app."""
        return TestClient(required_key_app)
    
    def test_missing_key_returns_error(self, required_key_client: TestClient):
        """Test that missing key returns error when required."""
        response = required_key_client.post("/create")
        
        assert response.status_code == 400
        assert "Missing" in response.json()["message"]


class TestInMemoryIdempotencyStore:
    """Tests for InMemoryIdempotencyStore."""
    
    @pytest.mark.asyncio
    async def test_set_and_get(self):
        """Test storing and retrieving data."""
        store = InMemoryIdempotencyStore()
        
        await store.set("key1", {"data": "test"}, ttl=60)
        result = await store.get("key1")
        
        assert result == {"data": "test"}
    
    @pytest.mark.asyncio
    async def test_missing_key_returns_none(self):
        """Test that missing key returns None."""
        store = InMemoryIdempotencyStore()
        
        result = await store.get("nonexistent")
        
        assert result is None
    
    @pytest.mark.asyncio
    async def test_delete(self):
        """Test deleting data."""
        store = InMemoryIdempotencyStore()
        
        await store.set("key1", {"data": "test"}, ttl=60)
        await store.delete("key1")
        result = await store.get("key1")
        
        assert result is None

