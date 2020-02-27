import itertools
import urllib.request
import os
import random
from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

url="http://l.omegle.com/"
f=str(0)
data = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" ]

@app.route('/')
@cross_origin()
def one_post():
    finalurl=url+random.choice(data)+random.choice(data)+random.choice(data)+random.choice(data)+random.choice(data)+".png"
    return Response(finalurl)