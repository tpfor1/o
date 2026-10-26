"""Command-line entry point for Nameless.

This module stays thin: it parses arguments, sets up logging, and starts the
program. Later it will also be the place that builds the real pieces (the system
backend, the chosen LLM, ...) and passes them down, which keeps every other layer
free of knowledge about concrete implementations.

Exit codes: 0 success, 1 expected error, 2 bad arguments (argparse), 130 Ctrl+C.
"""

import argparse
import logging
import sys
from collections.abc import Sequence
from importlib.metadata import PackageNotFoundError, version

from nameless.errors import NamelessError

_DISTRIBUTION_NAME = "nameless"


def get_version() -> str:
    """Return the installed version of Nameless, read from the package metadata."""
    try:
        return version(_DISTRIBUTION_NAME)
    except PackageNotFoundError:
        return "unknown"


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        prog="nameless",
        description="Nameless, a fully autonomous butler",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {get_version()}")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="show detailed logs and full error tracebacks",
    )
    # Subcommands go here later, for example:
    #   subparsers = parser.add_subparsers(dest="command")
    #   subparsers.add_parser("doctor", help="print diagnostic information")
    return parser


def configure_logging(debug: bool) -> None:
    """Set up console logging. To be replaced by nameless.log once that exists."""
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.WARNING,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


def run(args: argparse.Namespace) -> None:
    """Start Nameless. Placeholder until the assistant loop exists."""
    print("Good morning, Sir")


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line interface and return the process exit code."""
    args = build_parser().parse_args(argv)
    configure_logging(args.debug)
    try:
        run(args)
    except KeyboardInterrupt:
        print(file=sys.stderr)
        return 130
    except NamelessError as exc:
        if args.debug:
            raise
        print(f"error: {exc}", file=sys.stderr)
        if exc.hint:
            print(f"hint: {exc.hint}", file=sys.stderr)
        return 1
    return 0
