from flask import Flask, jsonify
from utils import get_by_title, get_films_by_year, children_films, family_films, adult_films, get_film_by_genre

app = Flask(__name__)

@app.route('/movie/<title>')
def movie_page(title):
    return get_by_title(title)


@app.route('/movie/<year_1>/to/<year_2>')
def year_page(year_1, year_2):
    film = get_films_by_year(year_1, year_2)
    return jsonify(film)

@app.route('/rating/<rating>')
def rating_page(rating):
    if rating == 'children':
        film = children_films()
    elif rating == 'family':
        film = family_films()
    elif rating == 'adult':
        film = adult_films()

    return jsonify(film)

@app.route('/genre/<genre>')
def page_genre(genre):
    film = get_film_by_genre(genre)
    return jsonify(film)

if __name__ == '__main__':
    app.run()
