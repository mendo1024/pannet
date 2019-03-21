#!/usr/bin/env python
from pyowm import OWM
import os
owm = OWM (os.environ["OPENWEATHER_API_KEY"])
observation = owm.weather_at_place(os.environ["CITY_NAME"])
w = observation.get_weather()
temperature = w.get_temperature(unit='fahrenheit')['temp']
detailed_status = w.get_detailed_status()
humidity = w.get_humidity()
print('sopurce=openweathermap, city="' + str(os.environ["CITY_NAME"]) + '", description="' + str(detailed_status) + '", temp=' + str(temperature) + ', humidity=' + str(humidity))
