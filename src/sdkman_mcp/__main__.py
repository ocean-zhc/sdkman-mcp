"""SDKMAN! MCP Server main entry point."""

import asyncio
import os
import sys
from importlib import metadata

from mcp.server.fastmcp import FastMCP

from .server import create_server


def main() -> None:
    """Run the SDKMAN! MCP Server."""
    try:
        version = metadata.version("sdkman-mcp")
    except metadata.PackageNotFoundError:
        from . import __version__ as version

    sdk_server = create_server()
    sdk_server.run()


if __name__ == "__main__":
    sys.exit(main()) 