# This project was created by: Ozzy
# This project was created on: 11/12/2019
import requests
import json
import humanize
import datetime

# This are a global variables with the Cities ID's.
CITIES_IDS = {
            3439525, 3439781, 3440645, 3442098, 3442778, 3443341, 3442233, 3441572, 3441575, 3443207, 3442546,
            3441287, 3441242, 3441686, 3441354, 3442057, 3442585, 3442727, 3439705, 3441890, 3443411, 3441684,
            3440711, 3440714, 3440696, 3441894, 3443173, 3441702, 3441665, 3440963, 3443413, 3440033, 3440034,
            3440571, 3443025, 3440789, 3442568, 3443737, 3440771, 3440777, 3442597, 3442587, 3441358, 3442980,
            3442750, 3443352, 3442051, 3441442, 3442398, 3443533, 3440942, 3442720, 3441273, 3442071, 3442105,
            3442683, 3441011, 3440925, 3440021, 3441292, 3480823, 3440379, 3442106, 3440063, 3442231, 3442926,
            3442050, 3440698, 3480819, 3442450, 3443632, 3441122, 3441475, 3440791, 3480818, 3439780, 3443861,
            3442805, 7838849, 3440581, 3440830, 3443756, 3443758, 3443013, 3439598, 3439619, 3439622, 3439652,
            3439659, 3439661, 3439725, 3439787, 3439831, 3439838, 3439902, 3440055, 3440076, 3440394, 3440541,
            3440554, 3440577, 3440580, 3440596, 3440653, 3440654, 3440705, 3440747, 3440762, 3440879, 3440939,
            3440985, 3441074, 3441377, 3441476, 3441481, 3441483, 3441577, 3441659, 3441674, 3441954, 3441988,
            3442058, 3442138, 3442206, 3442221, 3442236, 3442299, 3442716, 3442766, 3442803, 3442939, 3443061,
            3443183, 3443280, 3443289, 3443342, 3443356, 3443588, 3443631, 3443644, 3443909, 3443928, 3443952,
            3480812, 3480820, 3480822, 3480825, 3440781, 3440639, 3440054, 3442007, 3441243, 3439749, 3442163,
            3443030, 3439696, 3442584, 3440780, 3439590, 3439748, 3440400, 3440684, 3441114, 3441803, 3442238,
            3443256, 3443697
}


# This function will get the weather data from the API by city ID return the data to console.
def get_weather_data(city_id):
    api_key = 'a36f52ebcdb99aee27888350a630e12e'
    url = 'http://api.openweathermap.org/data/2.5/weather?id=' + str(city_id) + '&appid=' + api_key
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp'] - 273.15
    temp = humanize.intword(temperature) + '° Celsius '
    humidity = data['main']['humidity']
    weather = data['weather'][0]['main']
    city_name = data['name']
    ids = data['id']
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    print('The weather in ' + city_name + ' is ' + weather + ' with a temperature of ' + str(temp) +
         str(humidity) + '% of humidity' + ' and city id is ' + str(ids) + ' at ' + date)
    return [{'temperature': temp, 'humidity': humidity, 'weather': weather, 'city': city_name, 'date': date, 'id': ids}]


# This function runs cities_ids list and calls the get_weather_data function
def run_cities_ids():
    json_info = {}
    for city_id in CITIES_IDS:
        city_data = get_weather_data(city_id)
        json_info[city_id] = city_data
        json_write(json_info)
        json_info = json_read()


# This function writes the json file
def json_write(x):
    with open('information.json', 'w') as json_file:
        json.dump(x, json_file, indent=4, ensure_ascii=False)

# This function reads the json file
def json_read():
    with open('information.json') as information:
        data = json.load(information)
    return data


run_cities_ids()



