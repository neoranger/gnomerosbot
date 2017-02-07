# -*- coding: utf-8 -*-
import telebot # Library of API bot.
from telebot import types # Types from API bot
import codecs
import sys
from os.path import exists
import os
import token
import user
import feedparser
import owners
import logging
import commands
import subprocess
import requests

TOKEN = token.token_id
bot = telebot.TeleBot(TOKEN) # Creating our bot object.
bot.skip_pending=True

#Functions
@bot.message_handler(content_types=['new_chat_member'])
def command_new_user(m):
    cid = m.chat.id
    grupo = m.chat.title
    if (m.new_chat_member.username != None and m.new_chat_member.first_name != None and m.new_chat_member.last_name != None):
        bot.send_message(cid, 'Bienvenido' + ' ' + unicode(m.new_chat_member.first_name) + ' ' + unicode(m.new_chat_member.last_name) + '!! ' + ' A.K.A. ' + '@' + str(m.new_chat_member.username) + ' a ' + unicode(grupo) + '. ' + 'Te sugerimos leer las reglas en el mensaje anclado o click en #Normas.')
    elif (m.new_chat_member.username != None and m.new_chat_member.first_name == None and m.new_chat_member.last_name == None):
        bot.send_message(cid, 'Bienvenido' + ' ' + '!! ' + '@' + str(m.new_chat_member.username) + ' a ' + unicode(grupo) + '. ' + 'No tenés nombres, podrías completar los datos. Te sugerimos leer las reglas en el mensaje anclado o click en #Normas.')
    elif (m.new_chat_member.username != None and m.new_chat_member.first_name != None and m.new_chat_member.last_name == None):
        bot.send_message(cid, 'Bienvenido' + ' ' + unicode(m.new_chat_member.first_name) + '!!' + ' A.K.A. ' + '@' + str(m.new_chat_member.username) + ' a ' + unicode(grupo) + '. ' + 'Te sugerimos leer las reglas en el mensaje anclado o click en #Normas.')
    elif (m.new_chat_member.username != None and m.new_chat_member.first_name == None and m.new_chat_member.last_name != None):
        bot.send_message(cid, 'Bienvenido' + ' ' + unicode(m.new_chat_member.last_name) + '!!' + ' A.K.A. ' + '@' + str(m.new_chat_member.username) + ' a ' + unicode(grupo) + '. ' + 'Te sugerimos leer las reglas en el mensaje anclado o click en #Normas.')
    elif (m.new_chat_member.username == None and m.new_chat_member.first_name != None and m.new_chat_member.last_name != None):
        bot.send_message(cid, 'Bienvenido' + ' ' + unicode(m.new_chat_member.first_name) + ' ' + unicode(m.new_chat_member.last_name) + '!! ' + ' A ' + grupo + '. ' + 'No tenes alias, seria mejor que te crees uno. Te sugerimos tambien leer las reglas en el mensaje anclado o click en #Normas.')
    elif (m.new_chat_member.username == None and m.new_chat_member.first_name == None and m.new_chat_member.last_name != None):
        bot.send_message(cid, 'Bienvenido' + ' ' + unicode(m.new_chat_member.last_name) + '!! ' + ' a ' + grupo + '. ' + 'No tenes alias, seria mejor que te crees uno. Te sugerimos tambien leer las reglas en el mensaje anclado o click en #Normas.')
    elif (m.new_chat_member.username == None and m.new_chat_member.first_name != None and m.new_chat_member.last_name == None):
        bot.send_message(cid, 'Bienvenido' + ' ' + unicode(m.new_chat_member.first_name) + '!! ' + ' a ' + grupo + '. ' + 'No tenes alias, seria mejor que te crees uno. Te sugerimos tambien leer las reglas en el mensaje anclado o click en #Normas.')

@bot.message_handler(content_types=['left_chat_member'])
def command_left_user(m):
    cid = m.chat.id
    bot.send_message(cid, '@' + unicode(m.left_chat_member.username) + ' Gracias por pasar!! Bye!! ')
    
@bot.message_handler(commands=['help'])
def command_ayuda(m):
    cid = m.chat.id
    bot.send_message( cid, "Comandos Disponibles:\n /github\n /about\n /support\n /help\n") #

@bot.message_handler(commands=['about'])
def command_about(m):
    cid = m.chat.id
    bot.send_message( cid, 'Acerca de @GnomerosBot: Creado por NeoRanger - www.neositelinux.com')
    
@bot.message_handler(commands=['support'])
def command_support(m):
    markup = types.InlineKeyboardMarkup()
    itembtnneo = types.InlineKeyboardButton('NeoRanger', url="telegram.me/NeoRanger")
    itembtnblog = types.InlineKeyboardButton('URL Blog', url="http://www.neositelinux.com")
    itembtnrepo = types.InlineKeyboardButton('Repo Github', url="http://github.com/kernelpanicblog/manjarobot")
    markup.row(itembtnneo)
    markup.row(itembtnblog)
    markup.row(itembtnrepo)
    bot.send_message(m.chat.id, "Choose an option:", reply_markup=markup)
    
@bot.message_handler(commands=['github'])
def command_github(m):
    cid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    itembtngit = types.InlineKeyboardButton('GnomerosBot', url="http://github.com/neoranger/gnomerosbot")
    markup.row(itembtngit)
    bot.send_message(m.chat.id, 'Repositorio GITHUB:',reply_markup=markup)
    
###############################################################################
print('Bot Initiated')