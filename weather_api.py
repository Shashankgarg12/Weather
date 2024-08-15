import requests
import json
def find():
    city=input('enter the city of india ')
    a=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},%20IN&appid=cd2870d58ff85291c9b749445e6d09c9')
    weather_api_data=json.loads(a.text)
    des=weather_api_data['weather'][0]['description']
    temp=(int(weather_api_data['main']['temp']))-273.15
    hume=weather_api_data['main']['humidity']
    response=f'''temperature        :- {temp:.2f}
humidity           :- {hume}
weather conditions :- {des}'''
    return response

print(find())