import config
import telebot
import requests
import xml.etree.ElementTree as ET

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=['text'])
def send_echo (message):
##    bot.send_message(message.chat.id,message.text)
    
    ##берем xml с сайта ММВБ
    url = 'https://iss.moex.com/iss/engines/futures/markets/forts/boards/RFUD/securities/SiZ2.xml'
    root = ET.fromstring(requests.get(url).content)
    Price=root.find("data[2]/rows[1]/row[1]").attrib.get("LAST")
    bot.send_message(message.chat.id,"Последняя цена фьючерса SiZ2 = "+Price)

bot.polling (non_stop=True)
