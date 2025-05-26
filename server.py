from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

uri = "mongodb+srv://ISIRMovieCluster:ISIRMovieCluster@isirmoviecluster.rf8gpag.mongodb.net/?retryWrites=true&w=majority&appName=ISIRMovieCluster"
client = MongoClient(uri)
db = client["ISIRMovieDB"]
collection = db["ISIRMovieCluster"]

@app.route("/vote", methods=["POST"])
def vote():
    data = request.get_json()
    choice = data.get("choice")

if choice in ["D1", "D2", "D3"]:
    collection.insert_one({"choice": choice})
    return jsonify({"message": "Vote recorded!"}), 200
else:
    return jsonify({"error": "Invalid choice"}), 400

@app.route("/results", methods=["GET"])
def results():
    from collections import Counter
    all_votes = list(collection.find({}, {"_id": 0, "choice": 1}))
    counts = Counter(v["choice"] for v in all_votes)
    return jsonify(dict(counts))

if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=5000)