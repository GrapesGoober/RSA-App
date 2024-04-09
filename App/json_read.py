import json

with open("App\config.json", "r") as f:
    config = json.loads(f.read())
    print(config["n"])