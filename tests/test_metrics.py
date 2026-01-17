"""
Tests for Metrics middleware.
"""

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from src import MetricsMiddleware, MetricsConfig, MetricsCollector


@pytest.fixture
def metrics_app() -> FastAPI:
    """Create app with metrics middleware."""
    app = FastAPI()
    app.add_middleware(MetricsMiddleware)
    
    @app.get("/")
    async def root():
        return {"message": "Hello"}
    
    @app.get("/error")
    async def error():
        return {"error": True}, 500
    
    return app


@pytest.fixture
def metrics_client(metrics_app: FastAPI) -> TestClient:
    """Create test client for metrics app."""
    return TestClient(metrics_app)


class TestMetricsMiddleware:
    """Tests for MetricsMiddleware."""
    
    def test_metrics_endpoint_exists(self, metrics_client: TestClient):
        """Test that /metrics endpoint exists."""
        response = metrics_client.get("/metrics")
        
        assert response.status_code == 200
        assert "text/plain" in response.headers["Content-Type"]
    
    def test_metrics_contains_uptime(self, metrics_client: TestClient):
        """Test that metrics include uptime."""
        response = metrics_client.get("/metrics")
        
        assert "fastmvc_uptime_seconds" in response.text
    
    def test_request_counted(self, metrics_client: TestClient):
        """Test that requests are counted in metrics."""
        # Make some requests
        metrics_client.get("/")
        metrics_client.get("/")
        
        # Check metrics
        response = metrics_client.get("/metrics")
        
        assert "fastmvc_http_requests_total" in response.text


class TestMetricsCollector:
    """Tests for MetricsCollector."""
    
    def test_record_request(self):
        """Test recording a request."""
        config = MetricsConfig()
        collector = MetricsCollector(config)
        
        collector.record_request(
            method="GET",
            path="/test",
            status_code=200,
            latency=0.1,
            response_size=100,
        )
        
        json_metrics = collector.get_json_metrics()
        assert json_metrics["total_requests"] == 1
    
    def test_error_tracking(self):
        """Test that 5xx errors are tracked."""
        config = MetricsConfig()
        collector = MetricsCollector(config)
        
        collector.record_request(
            method="GET",
            path="/error",
            status_code=500,
            latency=0.1,
        )
        
        json_metrics = collector.get_json_metrics()
        assert json_metrics["total_errors"] == 1
    
    def test_prometheus_format(self):
        """Test Prometheus-compatible output format."""
        config = MetricsConfig()
        collector = MetricsCollector(config)
        
        collector.record_request("GET", "/test", 200, 0.1)
        
        metrics = collector.get_metrics()
        
        assert "# HELP" in metrics
        assert "# TYPE" in metrics


class TestMetricsConfig:
    """Tests for MetricsConfig."""
    
    def test_default_config(self):
        """Test default configuration values."""
        config = MetricsConfig()
        
        assert config.metrics_path == "/metrics"
        assert config.enable_latency_histogram is True
        assert config.enable_request_count is True
    
    def test_custom_histogram_buckets(self):
        """Test custom histogram buckets."""
        config = MetricsConfig(
            histogram_buckets=(0.1, 0.5, 1.0, 5.0),
        )
        
        assert config.histogram_buckets == (0.1, 0.5, 1.0, 5.0)

