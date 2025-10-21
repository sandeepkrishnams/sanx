# API Surface

This document lists the primary public interfaces you’ll use when embedding or extending sanx.

Primary types:

- `sanx.http.Request` — dataclass with fields: `method`, `path`, `headers`, `body`.
- `sanx.http.Response` — dataclass with `status`, `body`, `headers`, and `to_bytes()`.

Server:

- `sanx.run_server(host, port, app)` — start the example asyncio server. `app` is a `Router`
  instance with registered handlers.

Router:

- `Router.add(method, path, handler)` — register a handler callable. Handler signature: `async def handler(request) -> Response`.
- `Router.match(method, path) -> handler|None` — resolve a handler for an incoming request.

Middleware:

- Middleware are functions of the form `async def mw(request, handler) -> Response`.
- Compose middleware by passing them to Router or a composition helper (see `middleware.py`).
