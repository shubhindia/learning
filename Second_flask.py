from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/REST", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_request = request.get_json()
        return jsonify({"You Requested":some_request}), 201
    else:
        return jsonify({"Welcome":"Hello There"})


@app.route("/square/<int:num>", methods=['GET'])
def multiply(num):
    return jsonify({"square is":num*num})


if __name__ == '__main__':
    app.run(debug=True)
