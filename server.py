from mcp.server.fastmcp import FastMCP
import logging

# Log to stderr only (safe for stdio)
logging.basicConfig(level=logging.INFO)

mcp = FastMCP("my-tools")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers and return the sum."""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="stdio")
