# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def special_add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b + 100


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}! I'm Zhengpu"


# execute and return the stdio output
if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.settings.debug = True
    mcp.settings.log_level = "DEBUG"
    mcp.run("sse")
    print("Server finished.")  # This might not appear if server runs correctly
    
    
# python "C:/Users/zhaoz/OneDrive - moodys.com/ZZP_files/study-model-context-protocol/example/my_first_mcp_server/server.py"