from __future__ import annotations

import socket
import threading
from typing import Tuple

from sanx.exceptions import InvalidHostError, InvalidPortError, PortInUseError


class SanxServer:
    """A very small server placeholder used for examples and basic testing.
    """

    def __init__(self, host: str, port: int, blocking=True) -> None:
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
        """Verify server configuration."""
        self._validate_host()
        self._validate_port()

    def _validate_host(self) -> None:
        """Validate a Given Host

        Raises:
            InvalidHostError: return message indicating invalid host
        """
        if not isinstance(self.host, str) or not self.host:
            raise InvalidHostError("self.host")

    def _validate_port(self) -> None:
        """Validate a port

        Raises:
            InvalidPortError: return message indicating invalid port
        """
        if not isinstance(self.port, int) or not (0 < self.port < 65536):
            raise InvalidPortError(self.port)


    def initialize(self) -> None:
        """Prepare socket and internal structures."""
        # Validate host and port first
        if not isinstance(self.host, str) or not self.host:
            raise InvalidHostError(self.host)
        if not isinstance(self.port, int) or not (1 <= self.port <= 65535):
            raise InvalidPortError(self.port)

        # Create the socket
        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.settimeout(0.5)
        except OSError as e:
            # Typical errors: port in use or other OS-level socket errors
            if e.errno in (98, 48):  # 98=Linux, 48=Mac
                raise PortInUseError(self.port)
            else:
                raise ConnectionError(str(e))

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

        if self._socket:
            try:
                # Stop both send and receive
                self._socket.shutdown(socket.SHUT_RDWR)
            except OSError:
                # Socket may already be closed or never connected
                pass
            finally:
                self._socket.close()
                self._socket = None


def runserver(
    host: str = "127.0.0.1",
    port: int = 8080,
    blocking: bool = True,
) -> SanxServer:
    """Convenience function to run a SanxServer.

    Returns the created server instance. If block is True this function will
    not return until the server stops.
    """
    server = SanxServer(host=host, port=port)
    server.initialize()

    if blocking:
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
