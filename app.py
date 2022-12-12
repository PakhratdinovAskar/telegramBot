import telebot
import requests

token = '5827004330:AAF1YNVcc1Tdizicb5c3pM6OMADGlMvTVC4'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):

  button1 = telebot.types.KeyboardButton(text='USD - KZT')
  button2 = telebot.types.KeyboardButton(text='EUR - KZT')
  keyboard = telebot.types.ReplyKeyboardMarkup()
  keyboard.add(button1)
  keyboard.add(button2)

  bot.send_message(message.chat.id, "Узнать курс валют на сегодня", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def text_message(message):
  if message.text == 'USD - KZT':
    USDKZT = requests.get('https://currate.ru/api/?get=rates&pairs=USDKZT&key=b39f4f08ebd11d3a7e9f5b6a8f10798a').json()['data']['USDKZT']
    bot.send_message(message.chat.id, USDKZT)

  elif message.text == 'EUR - KZT':
    EURKZT = requests.get('https://currate.ru/api/?get=rates&pairs=EURKZT&key=b39f4f08ebd11d3a7e9f5b6a8f10798a').json()['data']['EURKZT']
    bot.send_message(message.chat.id, EURKZT)

bot.infinity_polling()


