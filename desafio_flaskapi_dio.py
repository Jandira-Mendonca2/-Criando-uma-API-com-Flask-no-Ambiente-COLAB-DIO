# -*- coding: utf-8 -*-
"""Desafio-FlaskApi-DIO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_AvV-DoNmCv_S9quzTeiddUMtaS-WVy9
"""

!pip install flask

!pip install flask_ngrok

from flask import *
import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random

# app = Flask(__name__)
# @app.route("/index")
# def home():
#   return "Hello world"

app = Flask(__name__)
run_with_ngrok(app)
@app.route("/index")
def home():
  return "Hello world"
  app.run

d = [{
    "Numero": 1,
    "Nome": "Mahesh",
    "Idade": 25,
    "Cidade": "Bangalore",
    "Pais": "India",
    },
     {
    "Numero": 2,
    "Nome": "Alex",
    "Idade": 26,
    "Cidade": "Londres",
    "Pais": "Reino Unido",
    },
     {
    "Numero": 3,
    "Nome": "David",
    "Idade": 27,
    "Cidade": "San Francisco",
    "Pais": "USA",
    },
     {
    "Numero": 4,
    "Nome": "John",
    "Idade": 28,
    "Cidade": "Toronto",
    "Pais": "Canada",
    },
    {
    "Numero": 5,
    "Nome": "Chris",
    "Idade": 29,
    "Cidade": "Paris",
    "Pais": "França",
    }
]

import flask
@app.route("/")
def index():
    return "<marquee><h3> TO CHECK IN PUT ADD '/input' TO THE URL AND TO CHECK OUT PUT ADD '/output' TO THE URL.</h3></marquee>"

@app.route("/input")
def input():
  return jsonify(d)

def predJson():
 pred = r.choice(["positive","negative"])
 nd = d # our input
 nd["prediction"]=pred
 return jsonify(nd)

 app.run()