from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/log-gpt-use", methods=["POST"])
def log_use():
    data = request.json
    with open("logs.txt", "a") as file:
        file.write(f"{datetime.now()} | {data}\n")
    return {"status": "ok"}, 200

app.run(host="0.0.0.0", port=5000)
