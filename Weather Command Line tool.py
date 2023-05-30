# Microsoft co pilot Github Hackathon

import json
import sys
import requests

if len(sys.argv) < 2:
    print("usage : weatherApp.py location")
    sys.exit()

location = ' '.join(sys.argv[1:])

# Download jon data from openweathermap.org API
url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=44d9c691134ba5174021daca67ace358" % location
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

data = weatherData['weather']
print("Weather of ", location, "is : ", data[0]['main'], " - ", data[0]['description'])

temperatureInCelsius = weatherData['main']

# print Temperature in degree celsius
print("Temperature is ", round(temperatureInCelsius['temp'] - 273, 2), "C")



