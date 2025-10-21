"""CLI entrypoint for sanx package."""
import argparse
import sys

from sanx.core import runserver


def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser(prog="sanx")
    parser.add_argument("--host", default="127.0.0.1", help="host to bind")
    parser.add_argument("--port", type=int, default=8080, help="port to bind")
    parser.add_argument("--version", action="store_true", help="print version and exit")
    args = parser.parse_args(argv)

    if args.version:
        try:
            from . import __version__
            print(__version__)
        except Exception:
            print("0.0.0")
        return 0

    # Start the server (blocking)
    runserver(host=args.host, port=args.port, block=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
