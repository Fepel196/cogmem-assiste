from flask import Flask, request
import os

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 5000))

@app.route("/", methods=["GET"])
def home():
    return "Hello, cogmem-api is running!"

if name == "__main__":
    app.run(host="0.0.0.0", port=PORT)
