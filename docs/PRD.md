# Product Requirements Document (PRD)

Project: sanx — Large-scale Python Async Web Server Skeleton

Author: (auto-generated)
Date: 2025-10-21

## Purpose

sanx is a from-scratch, practical Python web server skeleton designed for engineering teams that
want an async-first, minimal-dependency server with clear extension points for middleware, metrics,
tracing, secure TLS deployment, and a process worker model. This project is intentionally small but
production-minded and suitable as a learning codebase or a starting point for a microframework.

## Vision and Goals

- Provide a minimal, well-documented async HTTP server implementation using the Python standard
  library (asyncio) as the canonical reference implementation.
- Make it easy to swap components (router, request parser) with faster third-party libraries.
- Include robust features needed in production: TLS, graceful shutdown, connection/request timeouts,
  worker process supervision, and instrumentation hooks for metrics/tracing.
- Package and document the code for distribution (pyproject.toml, CI release workflow).

## Non-Goals

- Replace mature frameworks like FastAPI or aiohttp.
- Include a full WSGI/ASGI compatibility layer — the project focuses on demonstrating fundamentals.

## Key Features and Acceptance Criteria

1. Async core server using asyncio.start_server
   - Accepts TCP connections, parses HTTP/1.1 request line and headers, and dispatches to handler.
   - Test: unit test for core request handling with a fake stream.

2. Router
   - Compact trie-based router for fast path matching and parameter extraction.
   - Test: unit tests covering static and parameterized routes.

3. Middleware chain
   - Composable middleware functions: signature (request, handler) -> response / awaitable.

4. TLS support
   - Helper function to build an SSLContext from cert/key and recommended secure defaults.

5. Worker model
   - Process supervision script (worker.py) demonstrating prefork/master model for multiple CPUs.

6. Observability hooks
   - No-op `metrics.py` and `tracing` stubs that users can replace with Prometheus/OpenTelemetry.

7. Packaging & CI
   - `pyproject.toml` for modern packaging, GitHub Actions example to publish to TestPyPI.

## Stakeholders

- Engineers learning HTTP server internals
- Teams building minimal, embeddable HTTP services

## Risks and Mitigations

- Parsing/edge cases: keep tests for malformed inputs and timeouts.
- Security: default to strong TLS ciphers in `ssl_utils` and document key rotation.

## Timeline (high-level)

- Week 1: Core server, router, middleware, tests
- Week 2: TLS, worker model, docs, packaging
- Week 3: CI, publish to TestPyPI, gather feedback
