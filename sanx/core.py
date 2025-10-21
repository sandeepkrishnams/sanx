"""Minimal server with programmatic start/stop for CLI and imports.

This is intentionally simple: it starts a background TCP listener that accepts connections
and immediately closes them. Replace with a real server implementation as needed.
"""
import socket
import threading
import time
from contextlib import closing
from typing import Optional


class _ServerThread(threading.Thread):
    def __init__(self, host: str, port: int):
        super().__init__(daemon=True)
        self.host = host
        self.port = port
        self._sock: Optional[socket.socket] = None
        self._stop = threading.Event()

    def run(self):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen(5)
            self._sock = s
            while not self._stop.is_set():
                try:
                    s.settimeout(1.0)
                    conn, addr = s.accept()
                    conn.close()
                except OSError:
                    # timeout or socket closed
                    continue

    def stop(self):
        self._stop.set()
        if self._sock:
            try:
                self._sock.close()
            except Exception:
                pass


def runserver(host: str = "127.0.0.1", port: int = 8080, block: bool = True):
    """Start the server.

    If block is True (default), this call blocks until interrupted. If block is False,
    returns the ServerThread instance which can be stopped with .stop().
    """
    server = _ServerThread(host, port)
    server.start()
    print(f"sanx listening on {host}:{port}")
    if not block:
        return server
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop()


def serve_in_thread(host: str = "127.0.0.1", port: int = 8080):
    """Convenience wrapper returning the running server thread object."""
    return runserver(host, port, block=False)
