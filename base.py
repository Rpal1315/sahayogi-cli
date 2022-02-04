# import requests and json and webbrowser

import requests
import json
import webbrowser
from googletrans import Translator, constants
from pprint import pprint

# Make a main function to run the program
q = ""


def main(q):
    '''Main function to run the program'''

    def weather(i):
        '''Function to get weather data'''
        # Enter the API key
        api_key = '<your-openweathermap-api-key-here>'

        # base url
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'

        # give the city name
        city_name = i

        # complete url
        complete_url = base_url + 'appid=' + api_key + '&q=' + city_name

        # get the data
        response = requests.get(complete_url)

        # convert the data into json format
        x = response.json()

        # print the data
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature = round(current_temperature - 273.15, 0)
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]

            # store the value of variable z in variable weather_description
            weather_description = z[0]["description"]

            weather.resp = (" Temperature  = " +
                            str(current_temperature) + " C"
                            "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                            "\n humidity (in percentage) = " +
                            str(current_humidity) +
                            "\n description = " +
                            str(weather_description))

        else:
            weather.resp = " City Not Found "

    # make a function called search
    def search(i):
        '''Function to search google'''
        # make a url
        i = i.replace(" ", "+")
        url = "https://www.google.com/search?q=" + i
        # open the url in the default browser
        webbrowser.open(url)

    # make a function to tell jokes
    def joke():
        '''Function to tell jokes'''
        url = "https://icanhazdadjoke.com/"
        # get the data
        response = requests.get(url, headers={"Accept": "application/json"})
        # convert the data into json format
        x = response.json()
        # print the data
        joke.resp = x["joke"]

    def wiki(i):
        '''Function to search wikipedia'''
        i = i.replace(" ", "_")
        url = "https://en.wikipedia.org/wiki/" + i
        webbrowser.open(url)

    # make a function to check the date
    def date():
        '''Function to check the date'''
        import datetime
        date.resp = datetime.datetime.now()

    # make a function to translate from a language to another
    def translate(input_text, target_language):
        '''Function to translate from a language to another'''
        langs = {"arabic": "ar", "chinese": "zh-CN", "english": "en", "hindi": "hi", "japanese": "ja", "korean": "ko",
                 "portuguese": "pt", "russian": "ru", "spanish": "es", "turkish": "tr"}
        i = input_text
        lang_code = langs[target_language]
        translator = Translator()
        detection = translator.detect(i)
        src_lang = detection.lang
        translation = translator.translate(i, src=src_lang, dest=lang_code)
        translate.resp = translation.text

    # make a function to get the meaning of a word
    def meaning(i):
        '''Function to get the meaning of a word'''
        url = "https://api.datamuse.com/words?ml=" + i
        response = requests.get(url)
        x = response.json()
        if x == []:
            meaning.resp = "Word Not Found"
        else:
            meaning.resp = x[0]["word"]
    # make a function to respond to hello
    def hello():
        '''Function to respond to hello'''
        hello.resp = "Hello!I am your personal assistant.How can I help you?"
    # call main function
    if "weather" in q:
        q = q.replace("weather", "")
        q = q.split(" ")
        weather(q[2])
        main.respn = weather.resp
    elif "search" in q:
        q = q.replace("search", "")
        search(q)
    elif "joke" in q:
        joke()
        main.respn = joke.resp
    elif "wiki" in q:
        q = q.replace("wiki", "")
        wiki(q)
    elif "date" in q:
        date()
        main.respn = date.resp
    elif "translate" in q:
        q = q.removeprefix("translate")
        q = q.split(" ")
        translate(q[1], q[3])

        main.respn = translate.resp
    elif "meaning" in q:
        q = q.removeprefix("meaning")
        q = q.split(" ")
        q = q[2]
        meaning(q)
        main.respn = meaning.resp
    elif "hello" in q:
        hello()
        main.respn = hello.resp
    else:
        main.respn = " Invalid command "


