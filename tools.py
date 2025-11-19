from mcp.server import tool

@tool()
def add_numbers(a: int, b: int):
    """두 수를 더합니다."""
    return {"result": a + b}

TOOLS = [add_numbers]
