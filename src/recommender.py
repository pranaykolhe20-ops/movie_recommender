import pickle
import pandas as pd
import requests
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

movies_dict = pickle.load(open(os.path.join(BASE_DIR, "Data/processed/movies_dict.pkl"), "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open(os.path.join(BASE_DIR, "Data/processed/similarity.pkl"), "rb"))

API_KEY = os.getenv("TMDB_API_KEY")

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "language": "en-US"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
    except:
        pass

    return "https://via.placeholder.com/300x450?text=No+Poster"


def recommend(movie_title):
    movie_index = movies[movies["title"] == movie_title].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    results = []

    for i in movies_list:
        results.append({
            "title": movies.iloc[i[0]].title,
            "poster": fetch_poster(movies.iloc[i[0]].movie_id)
        })

    return results
