import json

def get_private_key() -> tuple[int, int]:
    with open("private_key.json", "r") as f:
        keys = json.loads(f.read())["keys"]
    return keys

def get_public_key(name: str) -> int:
    with open("public_key.json", "r") as f:
        keys = json.loads(f.read())
    if name not in keys:
        return None
    return keys[name]