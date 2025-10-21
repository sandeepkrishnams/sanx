"""sanx package public API."""

__version__ = "1.0.0"

__all__ = ["runserver", "serve_in_thread", "main"]

# The package entrypoint lives in __main__.py for CLI execution; re-export
# its `main` so scripts that import `sanx.main` (console scripts) work.
from sanx.__main__ import main

# Re-export the package public API from submodules so consumers (and the
# console-script wrapper) can import symbols from the package root.
from sanx.core import runserver, serve_in_thread
