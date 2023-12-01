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

bot = telebot.TeleBot('6975514591:AAHoIVGVBW3nbLHGhjbBN1Q1-EYHohTB11c')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("СПИСОК КОМАНД")
    markup.add(btn1)
    bot.send_message(message.from_user.id, '<b> 👋 Привет!Список команд в панели! </b> ', parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'СПИСОК КОМАНД':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Как стать успешным?')
        btn2 = types.KeyboardButton('Пустота')
        btn3 = types.KeyboardButton('Правила использования')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓Выбери категорию❓', reply_markup=markup) #ответ бота


    elif message.text == 'Как стать успешным?':
        bot.send_message(message.from_user.id, 'Надо купить курсы у меня в тг, мой ник - @Official_Snakeee')

    elif message.text == 'Пустота':
        bot.send_message(message.from_user.id, 'Здесь пока ничего нет.')

    elif message.text == 'Правила использования':
        bot.send_message(message.from_user.id, '1) Не быть пидором'
                                               '2) Не быть гандоном'
                                               '3) Не быть дотером')


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