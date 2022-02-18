import telebot
import requests
import json


Token = open("token.txt", "r").read()
Api_key = open("apikey.txt", "r").read()

bot = telebot.TeleBot(Token)


def weather(text):
    resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+text+'&appid='+Api_key)
    if resp.status_code == 200:
        data = json.loads(resp.content.decode('UTF-8'))
        name = 'Weather in the city ' + data['name'] + ' \n \n '
        temp = 'Temperature:' + str(int(round(data['main']['temp'] - 273))) + '° C \n '
        state = 'State: ' + data['weather'][0]['description'] + ' \n '
        wind = 'Wind: '+str(data['wind']['speed'])+' m/s\n'
        return name+temp+state+wind
    else:
        return 'Can not find city ' + text


@bot.message_handler(commands=['start'])
def start_message(message):
    bot . send_message ( message.chat.id,'Hello, write me the name of the city in English and I will find the weather '
                                         'forecast.')


@ bot . message_handler(func=lambda n: True)
def fun(message):
    bot.send_message(message.chat.id, weather(message.text))

try:
    bot.polling(none_stop=True, timeout=50)
except:
    pass