from telegram.ext import Updater, CommandHandler, MessageHandler, PrefixHandler, Filters
import os
import random


USER_TOKEN = "1192138822:AAHEaTn8e4aLRHCBYbiIgvA26mCYvnsQHy4"


def start(bot, context):
    bot.message.reply_text("Хуярт")


def run_bot():
    updater = Updater(USER_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))  # создается обработчик команды старт
    dispatcher.add_handler(CommandHandler("math", math))
    dispatcher.add_handler(PrefixHandler("#", "random", get_num))
    dispatcher.add_handler(PrefixHandler("#", "count", get_count))
    dispatcher.add_handler(MessageHandler(Filters.text, message)) # создается обработчик простого сообщения
    updater.start_polling() #создает несколько подключений к апи и запускаетсяя проверка
    updater.idle()


def math(bot, context):
    value = " ".join(context.args) #забираем данные ВМЕСТЕ с командой
    result = eval(value)
    bot.message.reply_text(result)


def message(bot, context):
    text = bot.message.text
    text = text.lower()
    hyext = text[::-1]




    if text == "привет":
        bot.message.reply_text("Хует")
    elif text == "ky":
        bot.message.reply_text("ky")
    else: bot.message.reply_text(hyext)



def get_count(bot, context):
    text = bot.message.text
    count = len(text) - 7
    bot.message.reply_text(str(count))


def get_num(bot, context):
    bot.message.reply_text(str(random.random(10)))


if __name__ == "__main__":
    run_bot()
