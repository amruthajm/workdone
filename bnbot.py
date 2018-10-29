import telebot
import requests
requests.timeout=30
bot = telebot.TeleBot("796794406:AAHGwnU0QHHpTNmJVUAxFD4k8bKC08GpP60")
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message,"how are you doing?")
@bot.message_handler(func=lambda message:True)
def echo_all(message):
	bot.reply_to(message,message.text)
@bot.message_handler(commands=["good"])
def send_welcome(message):
	bot.reply_to(message,"how was your day")
@bot.message_handler(func=lambda message:True)
def echo_all(message):
	bot.reply_to(message,message.text)
@bot.message_handler(commands=["not bad"])
def send_welcome(message):
	bot.reply_to(message,"Oh,then take some rest.Bye..!!")
@bot.message_handler(func=lambda message:True)
def echo_all(message):
	bot.reply_to(message,message.text)

bot.polling()
