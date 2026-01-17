# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in FastMVC Middleware, please report it responsibly:

1. **Do NOT** open a public GitHub issue for security vulnerabilities.

2. **Email** security concerns to: sengarsinghshivansh@gmail.com

3. **Include** in your report:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

4. **Response Time**:
   - Initial response: Within 48 hours
   - Status update: Within 5 business days
   - Fix timeline: Depends on severity

## Security Best Practices

When using FastMVC Middleware, we recommend:

### Authentication Middleware
- Use strong, randomly generated JWT secrets (256+ bits)
- Set appropriate token expiration times
- Rotate secrets periodically
- Use `HS256` or stronger algorithms

### Rate Limiting
- Set conservative limits for public endpoints
- Use stricter limits for authentication endpoints
- Monitor for rate limit bypass attempts

### Security Headers
- Enable HSTS in production (HTTPS only)
- Configure strict Content-Security-Policy
- Review and customize Permissions-Policy

### CORS
- Never use `allow_origins=["*"]` with credentials
- Explicitly list allowed origins in production
- Use regex patterns carefully

## Acknowledgments

We appreciate responsible disclosure and will acknowledge security researchers in our changelog (with permission).

