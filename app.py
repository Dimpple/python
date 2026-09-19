from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Python", 
        "env": os.getenv("APP_ENV", "development")
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # MUST be 0.0.0.0, not localhost, so the container is reachable
    app.run(host="0.0.0.0", port=8080)
