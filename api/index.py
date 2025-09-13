from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello from Flask on Vercel!"})

@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    return jsonify({"greet": f"Hi {name}, Flask API di Vercel sukses!"})
