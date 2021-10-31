# This project was created by: Ozzy
# This project was created on: 11/12/2019

# Imports
import requests
import json
import humanize


""" This function will get the weather data from the API by city ID and print weather 
    temperature in celsius and humidity to json file and console"""


def get_weather_data(city_id):
    api_key = 'a36f52ebcdb99aee27888350a630e12e'
    url = 'http://api.openweathermap.org/data/2.5/weather?id=' + str(city_id) + '&appid=' + api_key
    response = requests.get(url)
    data = response.json()
    with open('weather_data.json', 'w') as outfile:
        json.dump(data, outfile)
    temperature = data['main']['temp'] - 273.15
    temp = humanize.intword(temperature)
    humidity = data['main']['humidity']
    weather = data['weather'][0]['main']
    city_name = data['name']
    print('The weather in ' + city_name + ' is ' + weather + ' with a temperature of ' + str(temp) +
          'º Celsius and ' + str(humidity) + '% of humidity')




city_id = input('Enter the city ID: ')
get_weather_data(city_id)











