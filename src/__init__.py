"""
FastMVC Middleware - Production-ready middlewares for FastAPI applications.

A collection of battle-tested, configurable middleware components for building
robust FastAPI/Starlette applications with security, observability, and
rate limiting built-in.
"""

from src.base import FastMVCMiddleware
from src.cors import CORSMiddleware
from src.logging import LoggingMiddleware
from src.timing import TimingMiddleware
from src.request_id import RequestIDMiddleware
from src.security import SecurityHeadersMiddleware, SecurityHeadersConfig
from src.rate_limit import (
    RateLimitMiddleware,
    RateLimitConfig,
    RateLimitStore,
    InMemoryRateLimitStore,
)
from src.authentication import (
    AuthenticationMiddleware,
    AuthConfig,
    AuthBackend,
    JWTAuthBackend,
    APIKeyAuthBackend,
)
from src.request_context import (
    RequestContextMiddleware,
    get_request_id,
    get_request_context,
)
from src.compression import (
    CompressionMiddleware,
    CompressionConfig,
)
from src.trusted_host import TrustedHostMiddleware
from src.error_handler import (
    ErrorHandlerMiddleware,
    ErrorConfig,
)
from src.health import (
    HealthCheckMiddleware,
    HealthConfig,
)
from src.idempotency import (
    IdempotencyMiddleware,
    IdempotencyConfig,
    IdempotencyStore,
    InMemoryIdempotencyStore,
)
from src.cache import (
    CacheMiddleware,
    CacheConfig,
)
from src.metrics import (
    MetricsMiddleware,
    MetricsConfig,
    MetricsCollector,
)
from src.maintenance import (
    MaintenanceMiddleware,
    MaintenanceConfig,
)

__version__ = "0.2.0"
__author__ = "Shiv"
__license__ = "MIT"

__all__ = [
    # Base
    "FastMVCMiddleware",
    
    # Core Middlewares
    "CORSMiddleware",
    "LoggingMiddleware",
    "TimingMiddleware",
    "RequestIDMiddleware",
    "SecurityHeadersMiddleware",
    "SecurityHeadersConfig",
    
    # Rate Limiting
    "RateLimitMiddleware",
    "RateLimitConfig",
    "RateLimitStore",
    "InMemoryRateLimitStore",
    
    # Authentication
    "AuthenticationMiddleware",
    "AuthConfig",
    "AuthBackend",
    "JWTAuthBackend",
    "APIKeyAuthBackend",
    
    # Request Context
    "RequestContextMiddleware",
    "get_request_id",
    "get_request_context",
    
    # Compression
    "CompressionMiddleware",
    "CompressionConfig",
    
    # Trusted Host
    "TrustedHostMiddleware",
    
    # Error Handling
    "ErrorHandlerMiddleware",
    "ErrorConfig",
    
    # Health Checks
    "HealthCheckMiddleware",
    "HealthConfig",
    
    # Idempotency
    "IdempotencyMiddleware",
    "IdempotencyConfig",
    "IdempotencyStore",
    "InMemoryIdempotencyStore",
    
    # Caching
    "CacheMiddleware",
    "CacheConfig",
    
    # Metrics
    "MetricsMiddleware",
    "MetricsConfig",
    "MetricsCollector",
    
    # Maintenance Mode
    "MaintenanceMiddleware",
    "MaintenanceConfig",
]
