# Импортируем нужные компоненты (Updater - для подключения, CommandHandler - для "старта")
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater("652878300:AAGUfDk0w7jkbvp3IQvdfrDmR9DZlKZ5JOE", request_kwargs=PROXY)
    dp = mybot.dispatcher  # соединяет юзеров
    dp.add_handler(CommandHandler("start", greet_user))   # добавляем обработчика
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)
    # print('Вызван /start')
    # print(update)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


# Вызываем функцию - эта строчка собственно запускает бота
main()
