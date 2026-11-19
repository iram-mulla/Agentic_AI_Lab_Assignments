SAFE_DIRECTORY = "/safe/"
MOCK_FILES = {"/safe/README.md": "safe content"}

def read_file(path):
    if not path.startswith(SAFE_DIRECTORY):
        return {"error": "path outside safe directory"}
    if path not in MOCK_FILES:
        return {"error": "file not found"}
    return {"content": MOCK_FILES[path]}

print(read_file("/safe/README.md"))
print(read_file("/etc/passwd"))
