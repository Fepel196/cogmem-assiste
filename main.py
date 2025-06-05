import json
from flask import Flask, request

app = Flask(__name__)
MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route("/save", methods=["POST"])
def save():
    content = request.json
    memory = load_memory()
    user_id = str(content.get("user_id"))
    message = content.get("message")
    if user_id and message:
        memory[user_id] = memory.get(user_id, []) + [message]
        save_memory(memory)
        return {"status": "saved"}
    return {"status": "error", "detail": "Invalid input"}

@app.route("/memory/<user_id>", methods=["GET"])
def get_memory(user_id):
    memory = load_memory()
    return {"memory": memory.get(user_id, [])}

@app.route("/")
def home():
    return "🧠 Cognitive Memory System API is running."

if name == "__main__":
    app.run(host="0.0.0.0", port=10000)
