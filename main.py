from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "🤖 CogMem Assistant is running!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("🔔 Получен вебхук:", data)
    return "ok", 200

if name == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
