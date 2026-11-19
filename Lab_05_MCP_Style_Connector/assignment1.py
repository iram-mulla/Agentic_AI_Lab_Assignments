from reference import MCPServer, MCPClient

CAPABILITIES = [
    {"name": "read_file", "kind": "resource", "input": {"path": "str"}, "output": {"content": "str"}},
    {"name": "query_db", "kind": "tool", "input": {"sql": "str"}, "output": {"rows": "list"}},
    {"name": "list_files", "kind": "resource", "input": {}, "output": {"files": "list"}},
]
FILES = ["README.md", "guide.txt"]

MCPServer.list_capabilities = lambda self: CAPABILITIES
MCPServer.list_files = lambda self: {"files": FILES}

client = MCPClient(MCPServer(), "planning_agent")
manifest = client.discover()
print({"discovered": manifest})
print({"call_result": client.call("list_files")})
