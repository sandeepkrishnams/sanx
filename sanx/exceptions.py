class SanxError(Exception):
    """Base exception class for sanx package."""

    pass

class SanxError(Exception):
    """Base class for all Sanx exceptions."""
    pass

class PortInUseError(SanxError):
    """Raised when the specified port is already in use."""

    def __init__(self, port: int) -> None:
        super().__init__(f"Port {port} is already in use.")

class InvalidHostError(SanxError):
    """Raised when the specified host is invalid."""

    def __init__(self, host: str) -> None:
        super().__init__(f"Host '{host}' is invalid.")

class InvalidPortError(SanxError):
    """Raised when the specified port is invalid."""

    def __init__(self, port: int) -> None:
        super().__init__(f"Port '{port}' is invalid. Must be between 1 and 65535.")

class ConnectionError(SanxError):
    """Raised when there is a connection error."""

    def __init__(self, message: str) -> None:
        super().__init__(f"Connection error: {message}")

class SocketConnectionRefusedError(ConnectionError):
    """Raised when a socket connection is refused."""

    def __init__(self, host: str, port: int) -> None:
        super().__init__(f"Connection to {host}:{port} refused.")

class SocketTimeoutError(ConnectionError):
    """Raised when a socket connection times out."""

    def __init__(self, host: str, port: int) -> None:
        super().__init__(f"Connection to {host}:{port} timed out.")