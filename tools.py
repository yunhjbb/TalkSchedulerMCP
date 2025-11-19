from mcp.types import Tool, ToolDefinition, ToolInputSchema

def get_tools():
    return [
        Tool(
            name="add_numbers",
            description="두 숫자를 더한다.",
            input_schema=ToolInputSchema(
                type="object",
                properties={
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                required=["a", "b"]
            ),
            func=lambda args: {"result": args["a"] + args["b"]},
        )
    ]
