from flask import Flask, request, redirect, url_for, render_template
from movies import models
from movies import pref_key_generator
from movies import recommendation_maker

app = Flask(__name__)
models.start_mappers()

#homepage temporal
@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200


#registrar usuario (recibe info de registro)
#aqui se eligen las cat de movies
@app.route("/register", methods=["GET"])
def register():
    return "Welcome to IMDB app", 200

@app.route("/")
def index():
    return render_template("login.html")

#regresa user_id, recibe credenciales de usuario (username / password)
@app.route("/login", methods=["POST"])
def login():
    #return "<H1> You have logged in <H1>", 200
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
    if rating:
        print("rating is true/ on")
        movie_recommendations = recommendation_maker.recommend_with_true_rating(preference_key)
    else:
        print("rating is off")
        movie_recommendations = recommendation_maker.recommend_with_false_rating(preference_key)

    
    
    

    

    
    
    return "<H3> Welcome %s, with magic key %d </H3> <br> Your recommendations are: %s" %(uname,preference_key,movie_recommendations)


 
  


@app.route("/logout", methods=["GET"])
def logout():
    return "You have logged out", 200

#retornar las recomendaciones (recibe usuario y parametro rating- true/false-)
@app.route("/recommendations", methods=["GET"])
def recommendations():
    return "These are your recommendations", 200

#duda general
#corroborar si los usuarios deben guardarse y recuperarse de la DB