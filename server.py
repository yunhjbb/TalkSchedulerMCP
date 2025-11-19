from flask import Flask, request, jsonify
from mcp.server import MCPServer
from tools import TOOLS

app = Flask(__name__)

# 최신식 MCP 서버
server = MCPServer("my-mcp-server")

# tools.py에서 불러온 MCP Tools 등록
for t in TOOLS:
    server.register_tool(t)


@app.route("/mcp", methods=["POST"])
def mcp_endpoint():
    """OpenAI 모델의 MCP ToolCall을 처리하는 엔드포인트"""
    req = request.get_json()
    resp = server.handle_http(req)
    return jsonify(resp)


@app.route("/", methods=["GET"])
def index():
    return {"status": "running", "service": "MCP Server"}


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
