"""
FastMVC Middleware - Production-ready middlewares for FastAPI applications.

A comprehensive collection of 90+ battle-tested, configurable middleware components
for building robust FastAPI/Starlette applications.
"""

from fastMiddleware.base import FastMVCMiddleware

# ============================================================================
# Core Middlewares
# ============================================================================
from fastMiddleware.cors import CORSMiddleware
from fastMiddleware.logging import LoggingMiddleware
from fastMiddleware.timing import TimingMiddleware
from fastMiddleware.request_id import RequestIDMiddleware

# ============================================================================
# Security Middlewares
# ============================================================================
from fastMiddleware.security import SecurityHeadersMiddleware, SecurityHeadersConfig
from fastMiddleware.trusted_host import TrustedHostMiddleware
from fastMiddleware.csrf import CSRFMiddleware, CSRFConfig
from fastMiddleware.https_redirect import HTTPSRedirectMiddleware, HTTPSRedirectConfig
from fastMiddleware.ip_filter import IPFilterMiddleware, IPFilterConfig
from fastMiddleware.origin import OriginMiddleware, OriginConfig
from fastMiddleware.webhook import WebhookMiddleware, WebhookConfig
from fastMiddleware.referrer_policy import ReferrerPolicyMiddleware, ReferrerPolicyConfig
from fastMiddleware.permissions_policy import PermissionsPolicyMiddleware, PermissionsPolicyConfig
from fastMiddleware.csp_report import CSPReportMiddleware, CSPReportConfig
from fastMiddleware.replay_prevention import ReplayPreventionMiddleware, ReplayPreventionConfig
from fastMiddleware.request_signing import RequestSigningMiddleware, RequestSigningConfig
from fastMiddleware.honeypot import HoneypotMiddleware, HoneypotConfig
from fastMiddleware.sanitization import SanitizationMiddleware, SanitizationConfig

# ============================================================================
# Rate Limiting & Protection
# ============================================================================
from fastMiddleware.rate_limit import (
    RateLimitMiddleware,
    RateLimitConfig,
    RateLimitStore,
    InMemoryRateLimitStore,
)
from fastMiddleware.quota import QuotaMiddleware, QuotaConfig
from fastMiddleware.load_shedding import LoadSheddingMiddleware, LoadSheddingConfig
from fastMiddleware.bulkhead import BulkheadMiddleware, BulkheadConfig
from fastMiddleware.request_dedup import RequestDedupMiddleware, RequestDedupConfig
from fastMiddleware.request_coalescing import RequestCoalescingMiddleware, CoalescingConfig

# ============================================================================
# Authentication & Authorization
# ============================================================================
from fastMiddleware.authentication import (
    AuthenticationMiddleware,
    AuthConfig,
    AuthBackend,
    JWTAuthBackend,
    APIKeyAuthBackend,
)
from fastMiddleware.basic_auth import BasicAuthMiddleware, BasicAuthConfig
from fastMiddleware.bearer_auth import BearerAuthMiddleware, BearerAuthConfig
from fastMiddleware.scope import ScopeMiddleware, ScopeConfig
from fastMiddleware.route_auth import RouteAuthMiddleware, RouteAuthConfig, RouteAuth

# ============================================================================
# Session & Context
# ============================================================================
from fastMiddleware.session import (
    SessionMiddleware,
    SessionConfig,
    SessionStore,
    InMemorySessionStore,
    Session,
)
from fastMiddleware.request_context import (
    RequestContextMiddleware,
    get_request_id,
    get_request_context,
)
from fastMiddleware.correlation import (
    CorrelationMiddleware,
    CorrelationConfig,
    get_correlation_id,
)
from fastMiddleware.tenant import (
    TenantMiddleware,
    TenantConfig,
    get_tenant,
    get_tenant_id,
)
from fastMiddleware.context import (
    ContextMiddleware,
    ContextConfig,
    get_context,
    get_context_value,
    set_context_value,
)
from fastMiddleware.request_id_propagation import (
    RequestIDPropagationMiddleware,
    RequestIDPropagationConfig,
    get_request_ids,
    get_trace_header,
)

# ============================================================================
# Response Handling
# ============================================================================
from fastMiddleware.compression import CompressionMiddleware, CompressionConfig
from fastMiddleware.response_format import ResponseFormatMiddleware, ResponseFormatConfig
from fastMiddleware.cache import CacheMiddleware, CacheConfig
from fastMiddleware.etag import ETagMiddleware, ETagConfig
from fastMiddleware.data_masking import DataMaskingMiddleware, DataMaskingConfig, MaskingRule
from fastMiddleware.response_cache import ResponseCacheMiddleware, ResponseCacheConfig
from fastMiddleware.response_signature import ResponseSignatureMiddleware, ResponseSignatureConfig
from fastMiddleware.hateoas import HATEOASMiddleware, HATEOASConfig, Link
from fastMiddleware.bandwidth import BandwidthMiddleware, BandwidthConfig
from fastMiddleware.no_cache import NoCacheMiddleware, NoCacheConfig
from fastMiddleware.conditional_request import ConditionalRequestMiddleware, ConditionalRequestConfig
from fastMiddleware.early_hints import EarlyHintsMiddleware, EarlyHintsConfig, EarlyHint

# ============================================================================
# Error Handling
# ============================================================================
from fastMiddleware.error_handler import ErrorHandlerMiddleware, ErrorConfig
from fastMiddleware.circuit_breaker import CircuitBreakerMiddleware, CircuitBreakerConfig, CircuitState
from fastMiddleware.exception_handler import ExceptionHandlerMiddleware, ExceptionHandlerConfig

# ============================================================================
# Health & Monitoring
# ============================================================================
from fastMiddleware.health import HealthCheckMiddleware, HealthConfig
from fastMiddleware.metrics import MetricsMiddleware, MetricsConfig, MetricsCollector
from fastMiddleware.profiling import ProfilingMiddleware, ProfilingConfig
from fastMiddleware.audit import AuditMiddleware, AuditConfig, AuditEvent
from fastMiddleware.response_time import ResponseTimeMiddleware, ResponseTimeConfig, ResponseTimeSLA
from fastMiddleware.server_timing import (
    ServerTimingMiddleware,
    ServerTimingConfig,
    timing,
    add_timing,
)
from fastMiddleware.request_logger import RequestLoggerMiddleware, RequestLoggerConfig
from fastMiddleware.cost_tracking import (
    CostTrackingMiddleware,
    CostTrackingConfig,
    get_request_cost,
    add_cost,
)
from fastMiddleware.request_sampler import (
    RequestSamplerMiddleware,
    RequestSamplerConfig,
    is_sampled,
)

# ============================================================================
# Idempotency
# ============================================================================
from fastMiddleware.idempotency import (
    IdempotencyMiddleware,
    IdempotencyConfig,
    IdempotencyStore,
    InMemoryIdempotencyStore,
)

# ============================================================================
# Maintenance & Lifecycle
# ============================================================================
from fastMiddleware.maintenance import MaintenanceMiddleware, MaintenanceConfig
from fastMiddleware.warmup import WarmupMiddleware, WarmupConfig
from fastMiddleware.graceful_shutdown import GracefulShutdownMiddleware, GracefulShutdownConfig
from fastMiddleware.chaos import ChaosMiddleware, ChaosConfig
from fastMiddleware.slow_response import SlowResponseMiddleware, SlowResponseConfig

# ============================================================================
# Request Processing
# ============================================================================
from fastMiddleware.timeout import TimeoutMiddleware, TimeoutConfig
from fastMiddleware.request_limit import RequestLimitMiddleware, RequestLimitConfig
from fastMiddleware.trailing_slash import TrailingSlashMiddleware, TrailingSlashConfig, SlashAction
from fastMiddleware.content_type import ContentTypeMiddleware, ContentTypeConfig
from fastMiddleware.header_transform import HeaderTransformMiddleware, HeaderTransformConfig
from fastMiddleware.request_validator import RequestValidatorMiddleware, RequestValidatorConfig, ValidationRule
from fastMiddleware.json_schema import JSONSchemaMiddleware, JSONSchemaConfig
from fastMiddleware.payload_size import PayloadSizeMiddleware, PayloadSizeConfig
from fastMiddleware.method_override import MethodOverrideMiddleware, MethodOverrideConfig
from fastMiddleware.request_fingerprint import (
    RequestFingerprintMiddleware,
    FingerprintConfig,
    get_fingerprint,
)
from fastMiddleware.request_priority import RequestPriorityMiddleware, PriorityConfig, Priority

# ============================================================================
# URL & Routing
# ============================================================================
from fastMiddleware.redirect import RedirectMiddleware, RedirectConfig, RedirectRule
from fastMiddleware.path_rewrite import PathRewriteMiddleware, PathRewriteConfig, RewriteRule
from fastMiddleware.proxy import ProxyMiddleware, ProxyConfig, ProxyRoute

# ============================================================================
# API Management
# ============================================================================
from fastMiddleware.versioning import (
    VersioningMiddleware,
    VersioningConfig,
    VersionLocation,
    get_api_version,
)
from fastMiddleware.deprecation import DeprecationMiddleware, DeprecationConfig, DeprecationInfo
from fastMiddleware.retry_after import RetryAfterMiddleware, RetryAfterConfig
from fastMiddleware.api_version_header import APIVersionHeaderMiddleware, APIVersionHeaderConfig

# ============================================================================
# Detection & Analytics
# ============================================================================
from fastMiddleware.bot_detection import BotDetectionMiddleware, BotConfig, BotAction
from fastMiddleware.geoip import GeoIPMiddleware, GeoIPConfig, get_geo_data
from fastMiddleware.user_agent import (
    UserAgentMiddleware,
    UserAgentConfig,
    UserAgentInfo,
    get_user_agent,
)

# ============================================================================
# Feature Management & Testing
# ============================================================================
from fastMiddleware.feature_flag import (
    FeatureFlagMiddleware,
    FeatureFlagConfig,
    get_feature_flags,
    is_feature_enabled,
)
from fastMiddleware.ab_testing import (
    ABTestMiddleware,
    ABTestConfig,
    Experiment,
    get_variant,
)

# ============================================================================
# Localization & Content Negotiation
# ============================================================================
from fastMiddleware.locale import LocaleMiddleware, LocaleConfig, get_locale
from fastMiddleware.accept_language import (
    AcceptLanguageMiddleware,
    AcceptLanguageConfig,
    get_language,
)
from fastMiddleware.content_negotiation import (
    ContentNegotiationMiddleware,
    ContentNegotiationConfig,
    get_negotiated_type,
)
from fastMiddleware.client_hints import (
    ClientHintsMiddleware,
    ClientHintsConfig,
    get_client_hints,
)

# ============================================================================
# IP & Proxy Handling
# ============================================================================
from fastMiddleware.real_ip import RealIPMiddleware, RealIPConfig, get_real_ip
from fastMiddleware.xff_trust import XFFTrustMiddleware, XFFTrustConfig

__version__ = "0.5.0"
__author__ = "Shiv"
__email__ = "shiv@hyyre.dev"
__license__ = "MIT"
__url__ = "https://github.com/hyyre/fastmvc-middleware"

__all__ = [
    # Base
    "FastMVCMiddleware",
    
    # Core
    "CORSMiddleware",
    "LoggingMiddleware",
    "TimingMiddleware",
    "RequestIDMiddleware",
    
    # Security
    "SecurityHeadersMiddleware",
    "SecurityHeadersConfig",
    "TrustedHostMiddleware",
    "CSRFMiddleware",
    "CSRFConfig",
    "HTTPSRedirectMiddleware",
    "HTTPSRedirectConfig",
    "IPFilterMiddleware",
    "IPFilterConfig",
    "OriginMiddleware",
    "OriginConfig",
    "WebhookMiddleware",
    "WebhookConfig",
    "ReferrerPolicyMiddleware",
    "ReferrerPolicyConfig",
    "PermissionsPolicyMiddleware",
    "PermissionsPolicyConfig",
    "CSPReportMiddleware",
    "CSPReportConfig",
    "ReplayPreventionMiddleware",
    "ReplayPreventionConfig",
    "RequestSigningMiddleware",
    "RequestSigningConfig",
    "HoneypotMiddleware",
    "HoneypotConfig",
    "SanitizationMiddleware",
    "SanitizationConfig",
    
    # Rate Limiting & Protection
    "RateLimitMiddleware",
    "RateLimitConfig",
    "RateLimitStore",
    "InMemoryRateLimitStore",
    "QuotaMiddleware",
    "QuotaConfig",
    "LoadSheddingMiddleware",
    "LoadSheddingConfig",
    "BulkheadMiddleware",
    "BulkheadConfig",
    "RequestDedupMiddleware",
    "RequestDedupConfig",
    "RequestCoalescingMiddleware",
    "CoalescingConfig",
    
    # Authentication
    "AuthenticationMiddleware",
    "AuthConfig",
    "AuthBackend",
    "JWTAuthBackend",
    "APIKeyAuthBackend",
    "BasicAuthMiddleware",
    "BasicAuthConfig",
    "BearerAuthMiddleware",
    "BearerAuthConfig",
    "ScopeMiddleware",
    "ScopeConfig",
    "RouteAuthMiddleware",
    "RouteAuthConfig",
    "RouteAuth",
    
    # Session & Context
    "SessionMiddleware",
    "SessionConfig",
    "SessionStore",
    "InMemorySessionStore",
    "Session",
    "RequestContextMiddleware",
    "get_request_id",
    "get_request_context",
    "CorrelationMiddleware",
    "CorrelationConfig",
    "get_correlation_id",
    "TenantMiddleware",
    "TenantConfig",
    "get_tenant",
    "get_tenant_id",
    "ContextMiddleware",
    "ContextConfig",
    "get_context",
    "get_context_value",
    "set_context_value",
    "RequestIDPropagationMiddleware",
    "RequestIDPropagationConfig",
    "get_request_ids",
    "get_trace_header",
    
    # Response Handling
    "CompressionMiddleware",
    "CompressionConfig",
    "ResponseFormatMiddleware",
    "ResponseFormatConfig",
    "CacheMiddleware",
    "CacheConfig",
    "ETagMiddleware",
    "ETagConfig",
    "DataMaskingMiddleware",
    "DataMaskingConfig",
    "MaskingRule",
    "ResponseCacheMiddleware",
    "ResponseCacheConfig",
    "ResponseSignatureMiddleware",
    "ResponseSignatureConfig",
    "HATEOASMiddleware",
    "HATEOASConfig",
    "Link",
    "BandwidthMiddleware",
    "BandwidthConfig",
    "NoCacheMiddleware",
    "NoCacheConfig",
    "ConditionalRequestMiddleware",
    "ConditionalRequestConfig",
    "EarlyHintsMiddleware",
    "EarlyHintsConfig",
    "EarlyHint",
    
    # Error Handling
    "ErrorHandlerMiddleware",
    "ErrorConfig",
    "CircuitBreakerMiddleware",
    "CircuitBreakerConfig",
    "CircuitState",
    "ExceptionHandlerMiddleware",
    "ExceptionHandlerConfig",
    
    # Health & Monitoring
    "HealthCheckMiddleware",
    "HealthConfig",
    "MetricsMiddleware",
    "MetricsConfig",
    "MetricsCollector",
    "ProfilingMiddleware",
    "ProfilingConfig",
    "AuditMiddleware",
    "AuditConfig",
    "AuditEvent",
    "ResponseTimeMiddleware",
    "ResponseTimeConfig",
    "ResponseTimeSLA",
    "ServerTimingMiddleware",
    "ServerTimingConfig",
    "timing",
    "add_timing",
    "RequestLoggerMiddleware",
    "RequestLoggerConfig",
    "CostTrackingMiddleware",
    "CostTrackingConfig",
    "get_request_cost",
    "add_cost",
    "RequestSamplerMiddleware",
    "RequestSamplerConfig",
    "is_sampled",
    
    # Idempotency
    "IdempotencyMiddleware",
    "IdempotencyConfig",
    "IdempotencyStore",
    "InMemoryIdempotencyStore",
    
    # Maintenance & Lifecycle
    "MaintenanceMiddleware",
    "MaintenanceConfig",
    "WarmupMiddleware",
    "WarmupConfig",
    "GracefulShutdownMiddleware",
    "GracefulShutdownConfig",
    "ChaosMiddleware",
    "ChaosConfig",
    "SlowResponseMiddleware",
    "SlowResponseConfig",
    
    # Request Processing
    "TimeoutMiddleware",
    "TimeoutConfig",
    "RequestLimitMiddleware",
    "RequestLimitConfig",
    "TrailingSlashMiddleware",
    "TrailingSlashConfig",
    "SlashAction",
    "ContentTypeMiddleware",
    "ContentTypeConfig",
    "HeaderTransformMiddleware",
    "HeaderTransformConfig",
    "RequestValidatorMiddleware",
    "RequestValidatorConfig",
    "ValidationRule",
    "JSONSchemaMiddleware",
    "JSONSchemaConfig",
    "PayloadSizeMiddleware",
    "PayloadSizeConfig",
    "MethodOverrideMiddleware",
    "MethodOverrideConfig",
    "RequestFingerprintMiddleware",
    "FingerprintConfig",
    "get_fingerprint",
    "RequestPriorityMiddleware",
    "PriorityConfig",
    "Priority",
    
    # URL & Routing
    "RedirectMiddleware",
    "RedirectConfig",
    "RedirectRule",
    "PathRewriteMiddleware",
    "PathRewriteConfig",
    "RewriteRule",
    "ProxyMiddleware",
    "ProxyConfig",
    "ProxyRoute",
    
    # API Management
    "VersioningMiddleware",
    "VersioningConfig",
    "VersionLocation",
    "get_api_version",
    "DeprecationMiddleware",
    "DeprecationConfig",
    "DeprecationInfo",
    "RetryAfterMiddleware",
    "RetryAfterConfig",
    "APIVersionHeaderMiddleware",
    "APIVersionHeaderConfig",
    
    # Detection & Analytics
    "BotDetectionMiddleware",
    "BotConfig",
    "BotAction",
    "GeoIPMiddleware",
    "GeoIPConfig",
    "get_geo_data",
    "UserAgentMiddleware",
    "UserAgentConfig",
    "UserAgentInfo",
    "get_user_agent",
    
    # Feature Management & Testing
    "FeatureFlagMiddleware",
    "FeatureFlagConfig",
    "get_feature_flags",
    "is_feature_enabled",
    "ABTestMiddleware",
    "ABTestConfig",
    "Experiment",
    "get_variant",
    
    # Localization & Content Negotiation
    "LocaleMiddleware",
    "LocaleConfig",
    "get_locale",
    "AcceptLanguageMiddleware",
    "AcceptLanguageConfig",
    "get_language",
    "ContentNegotiationMiddleware",
    "ContentNegotiationConfig",
    "get_negotiated_type",
    "ClientHintsMiddleware",
    "ClientHintsConfig",
    "get_client_hints",
    
    # IP & Proxy Handling
    "RealIPMiddleware",
    "RealIPConfig",
    "get_real_ip",
    "XFFTrustMiddleware",
    "XFFTrustConfig",
]
