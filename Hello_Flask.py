from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "hello"

@app.route("/shubhi")
def hello_shubhi():
	return "hello shubhi"

@app.route("/shubhi/123")
def hello_shubhi123():
	return "hello shubhi 123"
if __name__ == "__main__":
	app.run(debug=True)
