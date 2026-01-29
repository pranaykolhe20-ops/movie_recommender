from flask import Flask, render_template, request
from src.recommender import movies, recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []

    if request.method == "POST":
        selected_movie = request.form.get("movie")
        recommendations = recommend(selected_movie)

    return render_template(
        "index.html",
        movie_list=movies["title"].values,
        recommendations=recommendations
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


