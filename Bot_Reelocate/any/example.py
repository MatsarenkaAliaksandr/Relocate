import random

import requests
import telebot
import webbrowser
import asyncio
import logging
import sys
import aiogram
import json


from telebot import types
from aiogram.types import InputFile

bot = telebot.TeleBot('7484203784:AAGB8lf8qSwGq9wlObdxyDr1xt-qM_qD17c')



def get_all_buttons():
    with open('menu.json', encoding='utf-8') as menu_config:
        config_data = json.load(menu_config)
    all_buttons = []
    for keyboard in config_data:
        for button in keyboard['buttons']:
            all_buttons.append(button)
    return all_buttons


def get_keyboard(keyboard_name):
    with open('menu.json', encoding='utf-8') as menu_config:
        config_data = json.load(menu_config)
    actual_keyboard = list(filter(lambda el: el['keyboard_name'] == keyboard_name, config_data))[0]
    keyboard = types.InlineKeyboardMarkup()
    buttons = sorted(actual_keyboard['buttons'], key = lambda el: int(el['id']))
    for button in buttons:
        keyboard.add(types.InlineKeyboardButton(button['name'], callback_data=button['id']))
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hello {message.from_user.full_name}', reply_markup=get_keyboard('main'))

@bot.callback_query_handler(func=lambda call:True)
def common_button(call):
    button = list(filter(lambda btn: call.data == btn['id'], get_all_buttons()))[0]
    bot.send_message(
        chat_id=call.message.chat.id,
        text='Hello',
        reply_markup=get_keyboard(button['next_keyboard']),
        parse_mode='html'
    )


bot.polling(non_stop=True, interval=0)
