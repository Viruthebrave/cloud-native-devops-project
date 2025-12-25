from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Cloud Native DevOps App is running")

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/predict")
def predict():
    return jsonify(result="Model prediction successful")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
