#!/usr/bin/python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
	return jsonify({"info":"hello"})

@app.route("/shubhi")
def hello_shubhi():
	return "hello shubhi"

@app.route("/shubhi/123")
def hello_shubhi123():
	return "hello shubhi 123"
if __name__ == "__main__":
	app.run(debug=True)
