from flask import Flask, request, redirect, url_for, render_template
from adapters import models
from domain import pref_key_generator
from domain import recommendation_maker

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
    key_generator = pref_key_generator.Preference_key_generator()
    preference_key = key_generator.get_pref_key(prefs)
    movie_recommendations =[]
    #rating parameter
    rating = request.form.get("rating")
    #ISP: We are segregating the ways in which to create the recommendations
    #LSP: pluggable types are the ways to do ratings
    recom_maker = recommendation_maker.Recommendation_Maker()
    if rating:
        print("rating is true/ on")
        #movie_recommendations = recommendation_maker.recommend_with_true_rating(preference_key)
        movie_recommendations = recom_maker.recommend_with_true_rating(preference_key)
    else:
        print("rating is off")
        #movie_recommendations = recommendation_maker.recommend_with_false_rating(preference_key)
        movie_recommendations = recom_maker.recommend_with_false_rating(preference_key)

    return "<H3> Welcome %s, with magic key %d </H3> <br> Your recommendations are: %s" %(uname,preference_key,movie_recommendations)
