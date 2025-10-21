# Architecture

Overview of the sanx design and components.

Components:

- core.py — asyncio-based TCP server and connection lifecycle. Responsible for reading request bytes,
  turning them into a `Request` object, running middleware+handler, and writing `Response` bytes.
- http.py — Request/Response dataclasses and a compact HTTP/1.1 parser.
- router.py — Trie-based router that matches URL paths and returns handler callables.
- middleware.py — Compose middleware into a single handler chain.
- worker.py — Optional multiprocess worker supervisor for prefork deployments.
- ssl_utils.py — Helpers to build secure `ssl.SSLContext` objects from certs.
- metrics.py — No-op hooks for metrics and tracing integrations.

Design decisions:

- Keep interfaces concrete and function-oriented (no ABCs) for simplicity and clarity.
- Async-first approach to leverage `asyncio` and be compatible with uvloop and other event loops.
- Minimal external dependencies — encourage substitution with high-performance libraries in production.
