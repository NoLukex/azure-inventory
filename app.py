from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(message="Azure Inventory API")


@app.get("/health")
def health():
    return jsonify(status="ok")

