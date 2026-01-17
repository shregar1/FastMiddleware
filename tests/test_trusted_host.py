"""
Tests for Trusted Host middleware.
"""

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from src import TrustedHostMiddleware


@pytest.fixture
def trusted_host_app(sample_routes) -> FastAPI:
    """Create app with trusted host middleware."""
    app = sample_routes
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["example.com", "www.example.com"],
    )
    return app


@pytest.fixture
def trusted_host_client(trusted_host_app: FastAPI) -> TestClient:
    """Create test client for trusted host app."""
    return TestClient(trusted_host_app)


class TestTrustedHostMiddleware:
    """Tests for TrustedHostMiddleware."""
    
    def test_valid_host_allowed(self, trusted_host_client: TestClient):
        """Test that valid host is allowed."""
        response = trusted_host_client.get(
            "/",
            headers={"Host": "example.com"}
        )
        assert response.status_code == 200
    
    def test_invalid_host_rejected(self, trusted_host_client: TestClient):
        """Test that invalid host is rejected."""
        response = trusted_host_client.get(
            "/",
            headers={"Host": "malicious.com"}
        )
        assert response.status_code == 400
        assert "Invalid host" in response.text


class TestWildcardHost:
    """Tests for wildcard host matching."""
    
    @pytest.fixture
    def wildcard_app(self, sample_routes) -> FastAPI:
        """Create app with wildcard host pattern."""
        app = sample_routes
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=["*.example.com"],
        )
        return app
    
    @pytest.fixture
    def wildcard_client(self, wildcard_app: FastAPI) -> TestClient:
        """Create test client for wildcard app."""
        return TestClient(wildcard_app)
    
    def test_wildcard_subdomain_allowed(self, wildcard_client: TestClient):
        """Test that subdomain matching works."""
        response = wildcard_client.get(
            "/",
            headers={"Host": "api.example.com"}
        )
        assert response.status_code == 200
    
    def test_base_domain_not_matched_by_wildcard(self, wildcard_client: TestClient):
        """Test that base domain is not matched by wildcard."""
        # *.example.com should not match example.com
        response = wildcard_client.get(
            "/",
            headers={"Host": "other.com"}
        )
        assert response.status_code == 400


class TestAllowAnyHost:
    """Tests for allowing any host."""
    
    @pytest.fixture
    def any_host_app(self, sample_routes) -> FastAPI:
        """Create app allowing any host."""
        app = sample_routes
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=["*"],
        )
        return app
    
    @pytest.fixture
    def any_host_client(self, any_host_app: FastAPI) -> TestClient:
        """Create test client for any host app."""
        return TestClient(any_host_app)
    
    def test_any_host_allowed(self, any_host_client: TestClient):
        """Test that any host is allowed with wildcard."""
        response = any_host_client.get(
            "/",
            headers={"Host": "anything.example.org"}
        )
        assert response.status_code == 200

