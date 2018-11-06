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

#######################################
#Function for feedparser
#CODE TAKEN FROM:
#https://gist.github.com/Jeshwanth/99cf05f4477ab0161349
def get_feed(url):
    try:
        feed = feedparser.parse(url)
    except:
        return 'Invalid url.'
    y = len(feed[ "items" ])
    y = 5 if y > 5 else y
    if(y < 1):
        return 'Nothing found'
    lines = ['*Feed:*']
    for x in range(y):
        lines.append('- [{}]({})'.format(feed['items'][x]['title'].replace(']', ':').replace('[', '').encode('utf-8'), feed['items'][x]['link']))
    return '\n'.join(lines)
#    for x in range(y):
#        lines.append(
#        u'-&gt <a href="{1}">{0}</a>.'.format(
#        u'' + feed[ "items" ][x][ "title" ],
#        u'' + feed[ "items" ][x][ "link" ]))
#    return u'' + '\n'.join(lines)

#######################################

#Functions
@bot.message_handler(content_types=['new_chat_members'])
def command_new_user(m):
    cid = m.chat.id
    grupo = m.chat.title
    markup = types.InlineKeyboardMarkup()
    itembtnnormas = types.InlineKeyboardButton("<Click Aquí>", url="https://t.me/gnomeros/4")
    markup.row(itembtnnormas)

    if (m.new_chat_member.username != None and m.new_chat_member.first_name != None and m.new_chat_member.last_name != None):
        bot.send_message(cid, "Bienvenido {0} {1} !! A.K.A. @{2} a {3}. Te sugerimos leer las reglas en el mensaje anclado o click en el botón.".format(m.new_chat_member.first_name, m.new_chat_member.last_name, m.new_chat_member.username, grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)
    elif (m.new_chat_member.username != None and m.new_chat_member.first_name == None and m.new_chat_member.last_name == None):
        bot.send_message(cid, "Bienvenido!! @{0} a {1}. No tenés nombres, podrías completar los datos. Te sugerimos leer las reglas en el mensaje anclado o click en el botón.".format(m.new_chat_member.username, grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)
    elif (m.new_chat_member.username != None and m.new_chat_member.first_name != None and m.new_chat_member.last_name == None):
        bot.send_message(cid, "Bienvenido {0} A.K.A. @{1} a {2}. Te sugerimos leer las reglas en el mensaje anclado o click en el botón.".format(m.new_chat_member.first_name,m.new_chat_member.username, grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)
    elif (m.new_chat_member.username != None and m.new_chat_member.first_name == None and m.new_chat_member.last_name != None):
        bot.send_message(cid, "Bienvenido {0}!! A.K.A. @{1} a {2}. Te sugerimos leer las reglas en el mensaje anclado o click en el botón.".format(m.new_chat_member.last_name,m.new_chat_member.username, grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)
    elif (m.new_chat_member.username == None and m.new_chat_member.first_name != None and m.new_chat_member.last_name != None):
        bot.send_message(cid, "Bienvenido {0} {1} a {2}. No tenes alias, seria mejor que te crees uno. Te sugerimos tambien leer las reglas en el mensaje anclado o click en el botón.".format(m.new_chat_member.first_name,m.new_chat_member.last_name,grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)
    elif (m.new_chat_member.username == None and m.new_chat_member.first_name == None and m.new_chat_member.last_name != None):
        bot.send_message(cid, "Bienvenido {0}!! a {1}. No tenes alias, seria mejor que te crees uno. Te sugerimos tambien leer las reglas en el mensaje anclado o click en el botón.".format(m.new_chat_member.last_name, grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)
    elif (m.new_chat_member.username == None and m.new_chat_member.first_name != None and m.new_chat_member.last_name == None):
        bot.send_message(cid, "Bienvenido {0} a {1}. No tenes alias, seria mejor que te crees uno. Te sugerimos tambien leer las reglas en el mensaje anclado o click en el botón.".format(m.new_chat_member.first_name, grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)

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

@bot.message_handler(commands=['gnomefeed'])
def gnome_feed(m):
    cid = m.chat.id
    url = str("https://gnome.org/feed/")
    print (url)
    bot.send_message(cid, get_feed(url),disable_web_page_preview=True,parse_mode="markdown")

@bot.message_handler(commands=['planetgnome'])
def planet_gnome(m):
    cid = m.chat.id
    url = str("https://planet.gnome.org/atom.xml")
    print (url)
    bot.send_message(cid, get_feed(url),disable_web_page_preview=True,parse_mode="markdown")

@bot.message_handler(commands=['kick'])
def command_kick_user(m):
        cid = m.chat.id
        uid = m.from_user.id
        if bot.get_chat_member(cid, uid).status in ["administrator", "creator"] and bot.get_chat_member(cid, m.reply_to_message.from_user.id).status not in ["administrator", "creator"]:
           bot.send_message(cid, 'Hasta la vista, Baby')
           bot.kick_chat_member(cid, m.reply_to_message.from_user.id)
    
###############################################################################
print('Bot Initiated')
