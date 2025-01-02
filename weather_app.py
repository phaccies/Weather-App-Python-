# Basic Weather App that fetches a given city's Weather using OpenWeatherAPI 

import requests #importing the api requests library

api_key = "3af4a26d58e45ec34c107c673c80f692"  #holds the api key from openweather 

city_name = input("Please enter your city: ")

#API fetch
data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&APPID={api_key}")

if data.status_code == 404:
    print("No city found.")

# print(data.json()) #this line lets you see the JSON Object so you know what you're working with

else:

    weather = data.json()['weather'][0]['main']  #if it's cloudly, clear, etc.
    temp = round(data.json()['main']['temp'])  #curr temp is
    feels_temp = round(data.json()['main']['feels_like']) #but it feels like
    hi_temp = round(data.json()['main']['temp_max'] )
    lo_temp = round(data.json()['main']['temp_min'])

    if weather == "Clouds":
        print(f"The weather in {city_name} is {temp} and there are {weather} in the sky.")
    else:
        print(f"The weather in {city_name} is {temp} and the sky is {weather}.")

    print(f"However, it feels more like {feels_temp}.")

    choice = input("Would you like to know the low and high for today? Y or N ")

    if choice == "Y" or choice == "y":
        print(f"The low for today is {lo_temp}")
        print(f"The high for today is {hi_temp}")
        print("Thanks for using!")

    else:
        print("Thanks for using!")
