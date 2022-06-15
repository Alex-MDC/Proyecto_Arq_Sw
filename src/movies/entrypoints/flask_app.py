from flask import Flask, request, redirect, url_for, render_template
from movies import models
from movies import pref_key_generator
from movies import recommendation_maker

# clean architecture: coupling is mostly related to the database, which currently is basically a local filem which would be updated with the webscraping
#modules are being created to carry the functionalities of the system to avoid higher coupling. for example preference key generation has its own module
# and also the recommendation creations has a kind of simple factory. the "switch" of the movie recommendation is the rating option as stated in the requirements.

app = Flask(__name__)
models.start_mappers()

#homepage temporal
@app.route("/ver", methods=["GET"])
def ver():
    return "Recommendation System V.1", 200

@app.route("/")
def index():
    return render_template("login.html")

#regresa user_id, recibe credenciales de usuario (username / password)
@app.route("/recommendations", methods=["POST"])
def recommendations():
    uname=request.form['uname']
    passwrd=request.form['pass']
    prefs =[]
    prefs.append(int(request.form['preference 1']))
    prefs.append(int(request.form['preference 2']))
    prefs.append(int(request.form['preference 3']))
    preference_key = pref_key_generator.get_pref_key(prefs)
    movie_recommendations =[]
    #rating parameter
    rating = request.form.get("rating")
    #ISP: We are segregating the ways in which to create the recommendations
    #LSP: pluggable types are the ways to do ratings
    if rating:
        print("rating is true/ on")
        movie_recommendations = recommendation_maker.recommend_with_true_rating(preference_key)
    else:
        print("rating is off")
        movie_recommendations = recommendation_maker.recommend_with_false_rating(preference_key)

    return "<H3> Welcome %s, with magic key %d </H3> <br> Your recommendations are: %s" %(uname,preference_key,movie_recommendations)
