from flask import Flask, request
from movies import models

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

#regresa user_id, recibe credenciales de usuario (username / password)
@app.route("/login", methods=["GET"])
def login():
    return "<H1> You have logged in <H1>", 200

@app.route("/logout", methods=["GET"])
def logout():
    return "You have logged out", 200

#retornar las recomendaciones (recibe usuario y parametro rating- true/false-)
@app.route("/recommendations", methods=["GET"])
def recommendations():
    return "These are your recommendations", 200

#duda general
#corroborar si los usuarios deben guardarse y recuperarse de la DB