from flask import Flask, request, jsonify
from data import data

app = Flask(__name__)

@app.route("/index")
def index():
    return jsonify({
        "data" : data,
        "message" : "sussces"
    }), 789

@app.route("/planet")

def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data" : planet_data,
        "message" : "sussces"
    }), 304

if __name__ == "__main__":
    app.run()