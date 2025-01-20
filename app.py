from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/weather" method="post">
            <input type="text" name="city" placeholder="Enter city name">
            <input type="submit" value="Get Weather">
        </form>
    '''

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = 'e65bfef89b563ade7dcbe09750dd8e4c' 
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f'Weather in {city}: {weather_description}, Temperature: {temperature}°C'
    else:
        return 'City not found.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
