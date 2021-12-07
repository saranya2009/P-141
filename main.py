from flask import Flask, jsonify, request
import csv

allArticles = []

with open("articles.csv", encoding="UTF8") as f:
    reader = csv.reader(f)
    data = list(reader)
    allArticles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)
@app.route("/get-article") 

def get_article():
    return jsonify({
        "data": allArticles[0],
        "status": "success"
    })

@app.route("/liked-article",methods=["POST"])

def liked_article():
    article = allArticles[0]
    liked_articles.append(article)
    allArticles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article",methods=["POST"])

def unliked_article():
    article = allArticles[0]
    not_liked_articles.append(article)
    allArticles.pop(0)
    return jsonify({
        "status": "success"
    }), 201


if __name__ == "__main__":
    app.run()