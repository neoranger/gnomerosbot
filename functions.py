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
import logging
import commands
import subprocess
import requests

TOKEN = token.token_id
bot = telebot.TeleBot(TOKEN) # Creating our bot object.
bot.skip_pending=True

#Functions
@bot.message_handler(content_types=['new_chat_members'])
def command_new_user(m):
    cid = m.chat.id
    grupo = m.chat.title
    if (m.new_chat_member.username != None and m.new_chat_member.first_name != None and m.new_chat_member.last_name != None):
        bot.send_message(cid, "Bienvenido {0} {1} !! A.K.A. @{2} a {3}. Te sugerimos leer las reglas en el mensaje anclado o click en #Normas.".format(m.new_chat_member.first_name, m.new_chat_member.last_name, m.new_chat_member.username, grupo))
    elif (m.new_chat_member.username != None and m.new_chat_member.first_name == None and m.new_chat_member.last_name == None):
        bot.send_message(cid, "Bienvenido!! @{0} a {1}. No tenés nombres, podrías completar los datos. Te sugerimos leer las reglas en el mensaje anclado o click en #Normas.".format(m.new_chat_member.username, grupo))
    elif (m.new_chat_member.username != None and m.new_chat_member.first_name != None and m.new_chat_member.last_name == None):
        bot.send_message(cid, "Bienvenido {0} A.K.A. @{1} a {2}. Te sugerimos leer las reglas en el mensaje anclado o click en #Normas.".format(m.new_chat_member.first_name,m.new_chat_member.username, grupo))
    elif (m.new_chat_member.username != None and m.new_chat_member.first_name == None and m.new_chat_member.last_name != None):
        bot.send_message(cid, "Bienvenido {0}!! A.K.A. @{1} a {2}. Te sugerimos leer las reglas en el mensaje anclado o click en #Normas.".format(m.new_chat_member.last_name,m.new_chat_member.username, grupo))
    elif (m.new_chat_member.username == None and m.new_chat_member.first_name != None and m.new_chat_member.last_name != None):
        bot.send_message(cid, "Bienvenido {0} {1} a {2}. No tenes alias, seria mejor que te crees uno. Te sugerimos tambien leer las reglas en el mensaje anclado o click en #Normas.".format(m.new_chat_member.first_name,m.new_chat_member.last_name,grupo))
    elif (m.new_chat_member.username == None and m.new_chat_member.first_name == None and m.new_chat_member.last_name != None):
        bot.send_message(cid, "Bienvenido {0}!! a {1}. No tenes alias, seria mejor que te crees uno. Te sugerimos tambien leer las reglas en el mensaje anclado o click en #Normas.".format(m.new_chat_member.last_name, grupo))
    elif (m.new_chat_member.username == None and m.new_chat_member.first_name != None and m.new_chat_member.last_name == None):
        bot.send_message(cid, "Bienvenido {0} a {1}. No tenes alias, seria mejor que te crees uno. Te sugerimos tambien leer las reglas en el mensaje anclado o click en #Normas.".format(m.new_chat_member.first_name, grupo))

@bot.message_handler(content_types=['left_chat_member'])
def command_left_user(m):
    cid = m.chat.id
    bot.send_message(cid, "@{0} Gracias por pasar!! Bye!!".format(left_chat_member.username))
    
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
    itembtnrepo = types.InlineKeyboardButton('Repo Github', url="http://github.com/neoranger")
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
