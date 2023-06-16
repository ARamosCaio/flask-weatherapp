from flask import Flask, render_template, jsonify
from flask_migrate import Migrate
from db import db
import requests
import models

app = Flask(__name__)


@app.route('/')

def get_data():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c6f160b7e998831a72aa93c83b0c5c26'
    cities = CityModel.objects.all()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : round((city_weather['main']['temp']-32)/1.8, 2),
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        
        weather_data.append(weather)

    context = {'weather_data' : weather_data}

    return render_template('index.html')

if __name__ == '__main__':
    app.run