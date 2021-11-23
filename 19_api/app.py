'''
FTC>FRC: Lucas Lee, Naomi Naranjo
Softdev
K19: REST APIs
2021-11-24
'''

from flask import Flask, render_template, request, session, redirect, url_for
import requests

app = Flask(__name__)

API_KEY = ""
URL = "https://api.nasa.gov/planetary/apod"

@app.route('/')
def show_image():

    r = requests.get(url=URL, params={'api_key': API_KEY})
    json = r.json()

    img = json['hdurl']
    explanation = json['explanation']

    return render_template('index.html', img=img, explanation=explanation)


if __name__ == '__main__':

    with open('key_nasa.txt') as f:
        key = f.readline().strip()
        API_KEY = key

    app.debug = True
    app.run()
