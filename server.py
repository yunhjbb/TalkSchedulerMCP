from flask import Flask, request, jsonify
from mcp.server import Server
from mcp.transport import StreamableServerTransport
from tools import get_tools

app = Flask(__name__)

# MCP 서버 생성
mcp_server = Server(name="my-mcp-server")

# 툴 등록
for tool in get_tools():
    mcp_server.add_tool(tool)


@app.route("/mcp", methods=["POST"])
def handle_mcp():
    """OpenAI/LLM이 MCP ToolCall을 보내는 엔드포인트"""
    req_json_str = request.data.decode("utf-8")

    response_sink = []
    transport = StreamableServerTransport(
        request=req_json_str,
        response_sink=response_sink
    )

    try:
        with mcp_server.connect(transport) as session:
            session.handle()

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(response_sink)


@app.route("/", methods=["GET"])
def index():
    return {"status": "MCP server is running."}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
