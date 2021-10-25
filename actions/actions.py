# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import os
from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_weather_search"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city=tracker.get_slot("location")
        complete_url="http://api.openweathermap.org/data/2.5/weather?"+"appid="+os.environ.get('api_key')+"&q="+city
        response = requests.get(complete_url)
        print(response.json())
        x = response.json()
        if x["cod"] == 200:
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            finstr=" Temperature (in kelvin unit) = "+str(current_temperature) +"K"+" \n Temperature (in Celcius unit) = "+str(current_temperature-273.15) +"°C"+"\n atmospheric pressure (in hPa unit) = "+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidity) +"%" + "\n description = " + str(weather_description)
        dispatcher.utter_message(text=finstr)
        return []
        