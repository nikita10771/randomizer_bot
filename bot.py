# #!/usr/bin/python
#
# # This is a simple echo bot using the decorator mechanism.
# # It echoes any incoming text messages.
#
# import telebot
#
# API_TOKEN = '6975514591:AAHoIVGVBW3nbLHGhjbBN1Q1-EYHohTB11c'
#
# bot = telebot.TeleBot(API_TOKEN)
#
#
# # Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message, """\
# Hello! This is Randomaizer_bot by Ryan Gosling, it will help you choose random things.\
# """)
#
#
# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# import random
#
# def randomize_option(option1, option2):
#     options = [option1, option2]
#     selected_option = random.choice(options)
#     return selected_option
#
# # Example usage
# option1 = "Option A"
# option2 = "Option B"
#
# selected_option = randomize_option(option1, option2)
# print("Selected option:", selected_option)
#
#
# bot.infinity_polling()

# import random
#
# def randomize_option(option1, option2):
#     options = [option1, option2]
#     selected_option = random.choice(options)
#     return selected_option
#
# # Example usage
# option1 = "Option A"
# option2 = "Option B"
#
# selected_option = randomize_option(option1, option2)
# print("Selected option:", selected_option)

import telebot
from telebot import types
import requests

bot = telebot.TeleBot('6975514591:AAHoIVGVBW3nbLHGhjbBN1Q1-EYHohTB11c')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Сommands")
    markup.add(btn1)
    bot.send_message(message.from_user.id, '<b> 👋 Hello! List of commands in the panel! </b> ', parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Сommands':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('How to become successful?💵')
        btn2 = types.KeyboardButton('Info🌐')
        btn3 = types.KeyboardButton('Help📕')
        btn4 = types.KeyboardButton('Just a minute joke😂')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '❓Select a category❓', reply_markup=markup) #ответ бота


    elif message.text == 'How to become successful?💵':
        bot.send_message(message.from_user.id, 'You need to buy courses from me in tg, my nickname - @Official_Snakeee')

    elif message.text == 'Info🌐':
        bot.send_message(message.from_user.id, 'Do you want to change your life for the better? Do you want to be able to travel, buy beautiful things and provide for your family? You may not be able to afford it right now, but there are ways to make money. Dont be afraid to dream more, set a goal and take action! Dont wait for the opportunity to come by itself, go meet it. Strive for success, learn new things, develop your skills and move forward confidently. The path to making money may be difficult, but you can overcome all obstacles and achieve your goal. Remember that you deserve the best, and you will succeed!')

    elif message.text == 'Help📕':
        bot.send_message(message.from_user.id, 'Support mail - platinum.academy.help@gmail.com .Tg - https://t.me/Platinum_Academy_Support')
    elif message.text == 'Just a minute joke😂':

        url = "https://v2.jokeapi.dev/joke/Programming"

        data = requests.get(url).json()
        if data['type'] == 'single':
            bot.send_message(message.from_user.id, data['joke'])
        else:
            bot.send_message(message.from_user.id, data['setup'])
            bot.send_message(message.from_user.id, data['delivery'])



bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть



# import telebot
# import random
# from telebot import types  # для создания кнопок
#
# bot = telebot.TeleBot('6975514591:AAHoIVGVBW3nbLHGhjbBN1Q1-EYHohTB11c')  # Token бота берётся из BotFather
#
#
# # Создание кнопки после команды Start
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     random_sender = types.KeyboardButton("Скинь Рандомное число")
#     markup.add(random_sender)
#     bot.send_message(message.chat.id, '<b>Привет! Это бот от Райана Гослинга и Киллиана Мёрфи. Мы поможем вам не умереть от скуки. </b> ', parse_mode='html',
#                      reply_markup=markup)
#
#
# # Отслеживание нажатий кнопки
# @bot.message_handler(content_types=['text'])
#
#
# def first_number_step(message):
#     if message.text == 'Скинь Рандомное число':
#         msg = bot.send_message(message.chat.id, 'Введите начало диапазона')
#         bot.register_next_step_handler(msg, second_number_step)             # переход на функцию second_number_step
#     else:
#         bot.send_message(message.chat.id, 'Такой команды нет')
#
#
# # Получение первого числа диапазона
# def second_number_step(message):
#     global NUM_first
#     NUM_first = int(message.text)
#     msg = bot.send_message(message.chat.id, 'Введите конец диапазона')
#     bot.register_next_step_handler(msg, result_number_step)                 # переход на функцию result_number_step
#
#
# # Получение второго числа диапазона
# def result_number_step(message):
#     global NUM_second
#     NUM_second = int(message.text)
#     result(message)                                                          # Вызов функции result(message)
#
#
# # Вывод результата (рандом)
# def result(message):
#     bot.send_message(message.chat.id, 'Случайное число:  ' + str(random.randint(NUM_first, NUM_second)))
#
#
# #Run
# bot.polling(none_stop=True)