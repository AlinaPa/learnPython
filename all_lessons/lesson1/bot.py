import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater("652878300:AAGUfDk0w7jkbvp3IQvdfrDmR9DZlKZ5JOE", request_kwargs=PROXY)
    dp = mybot.dispatcher  # соединяет юзеров
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", ask_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']


def greet_user(bot, update):
    text = 'Добрый день! Укажите планету, чтобы узнать в каком она созвездии, пример /planet Mars'
    print(text)
    update.message.reply_text(text)


def ask_planet(bot, update):
    try:
        planet = update.message.text.split('/planet ')[1]
    except IndexError:
        return
    planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto')
    if planet in planets:
        ephem_planet = getattr(ephem, planet)('2019/02/28')
        user_text = ephem.constellation(ephem_planet)
        print(user_text)
        update.message.reply_text(user_text)
    else:
        update.message.reply_text("Нет такой планеты")


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


main()
