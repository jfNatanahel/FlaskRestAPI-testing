#~movie-bag/app.py

from flask import Flask, jsonify
movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]

app = Flask(__name__)

@app.route('/movies') #Se incia un servidor 
def hello():
    return jsonify(movies)


app.run()
