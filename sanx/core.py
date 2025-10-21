from __future__ import annotations

import threading
from typing import Tuple


class SanxServer:
    """A very small server placeholder used for examples and basic testing.

    This class intentionally contains lightweight implementations so linters
    and type-checkers can reason about the public API. It is not a
    production-ready HTTP server.
    """

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self._socket = None
        self.is_running = False
        self._verify_configuration()

    def start(self) -> None:
        """Start the server (non-blocking)."""
        print(f"Starting Sanx server on {self.host}:{self.port}")
        self.is_running = True

    def _verify_configuration(self) -> None:
        # check if the host and port are valid
        self._validate_host()
        self._validate_port()

    def _validate_host(self) -> None:
        # Basic validation placeholder
        if not isinstance(self.host, str) or not self.host:
            raise ValueError("host must be a non-empty string")

    def _validate_port(self) -> None:
        # Basic validation placeholder
        if not isinstance(self.port, int) or not (0 < self.port < 65536):
            raise ValueError("port must be an int between 1 and 65535")

    def initialize(self) -> None:
        """Prepare sockets, state, and internal structures."""
        # placeholder for socket creation and other setup
        self._socket = None

    def serve_forever(self) -> None:
        """Main loop: accept and handle connections.

        This placeholder implementation only demonstrates the blocking
        behaviour expected by callers.
        """
        self.start()
        try:
            # simple blocking loop to simulate server activity
            while self.is_running:
                # In a real server we'd accept connections and handle requests.
                threading.Event().wait(0.1)
        finally:
            self.shutdown()

    def shutdown(self) -> None:
        """Cleanly close all connections and free resources."""
        self.is_running = False
        # placeholder: close sockets, release resources
        self._socket = None


def runserver(
    host: str = "127.0.0.1",
    port: int = 8080,
    block: bool = True,
) -> SanxServer:
    """Convenience function to run a SanxServer.

    Returns the created server instance. If block is True this function will
    not return until the server stops.
    """
    server = SanxServer(host=host, port=port)
    server.initialize()

    if block:
        server.serve_forever()
        return server

    # non-blocking: run in a daemon thread
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def serve_in_thread(
    host: str = "127.0.0.1",
    port: int = 8080,
) -> Tuple[SanxServer, threading.Thread]:
    """Start a server in a background thread and return (server, thread)."""
    server = SanxServer(host=host, port=port)
    server.initialize()
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread
