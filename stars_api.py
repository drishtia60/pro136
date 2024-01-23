from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

@app.route("/star")
def star():
    name = request.args.get("name")
    star_data = next((item for item in data if item["Star_name"] == name), None)
    if star_data:
        return jsonify({
            "data": star_data,
            "message": "success"
        }), 200
    return jsonify({
        "message": "Star not found"
    }), 404

if __name__ == "__main__":
    app.run()
