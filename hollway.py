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
    dispatcher.add_handler(PrefixHandler("/", "command", command))
    dispatcher.add_handler(PrefixHandler("/", "random", get_num))
    dispatcher.add_handler(PrefixHandler("/", "count", get_count))
    dispatcher.add_handler(PrefixHandler("!", "save", save_file))
    dispatcher.add_handler(PrefixHandler("!", "read", read_file))
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
        bot.message.reply_text("Привет")
    elif text == "ky":
        bot.message.reply_text("ky")
    else: bot.message.reply_text(hyext)



def get_count(bot, context):
    text = bot.message.text
    count = len(text) - 7
    bot.message.reply_text(str(count))


def command (bot, context):
    bot.message.reply_text("Используемые команды:\n"
                            "/command\n"
                            "/random\n"
                            "/command\n"
                            "!creation (file.txt) (info)\n"
                            "!read (file.txt)\n"
                            "!add (file.txt) (info)")


def get_num(bot, context):
    bot.message.reply_text(str(random.random(10)))


def save_file(bot, context):
    #print(context.args)
    file_name, text = context.args[0], " ".join(context.args[1:]) #через обычное открытие (обязательно закрыть файл!!)
    file = open(file_name, "w")
    res = file.write(text)
    bot.message.reply_text(str(res))
    file.close()



def read_file(bot, context):
    #print(context.args)
    file_name = context.args[0]
    with open(file_name):                            #через контекстный менеджер, не нужно закрывать файл
        bot.message.reply_text(file.read())


if __name__ == "__main__":
    run_bot()
