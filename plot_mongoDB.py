import time
from pymongo import MongoClient
import matplotlib.pyplot as plt

uri = "mongodb+srv://ISIRMovieCluster:ISIRMovieCluster@isirmoviecluster.rf8gpag.mongodb.net/?retryWrites=true&w=majority&appName=ISIRMovieCluster"
client = MongoClient(uri)
db = client["nome_database"]
collection = db["nome_collezione"]

while True:
    votes = collection.aggregate([
        {"$group": {"_id": "$choice", "count": {"$sum": 1}}}
    ])
    choices = []
    counts = []
    for vote in votes:
        choices.append(vote["_id"])
        counts.append(vote["count"])
    
    plt.clf()
    plt.bar(choices, counts)
    plt.title("Votes count")
    plt.pause(60)  # mostra grafico e aspetta 60 secondi per aggiornare
