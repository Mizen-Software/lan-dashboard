from flask import Flask, render_template
import requests
import json

# Create app object
app = Flask(__name__)

# Create index route
@app.route('/')

# Index render function
def index():
    return render_template('index.html')

# Weather
@app.route('/weather/')
def weather():
    openWeatherRequest = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London&APPID=6e7cdf71667535e7779477474ba2d890")
    return render_template('weather.html', weather = openWeatherRequest.content)

# Mysterious thing that makes it so other computers can view the server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
