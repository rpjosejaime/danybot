# -*- coding: utf-8 -*-
# @autor(es) Jose Jaime Rodriguez
# @nombre_archivo botelegram
# @fecha 16/04/2018
# @descripción Programa en telegram del proyecto

import telebot
from chatterbot import ChatBot

bot = telebot.TeleBot ("517451236:AAFtk1rbzPE_yVPYK8Utbv0uReLEHLSlQmY")

# @autor Jose Jaime Rodriguez
# @param message mensaje que se recibe del usuario
# @fecha_creacion 16/04/2018
def bot_conversacional(message):
	chatbot = ChatBot("Ejemplo Bot", 
	trainer = "chatterbot.trainers.ChatterBotCorpusTrainer",
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	database='LasMichesDeDany-database')
	respuesta = chatbot.get_response(message)
	if float (respuesta.confidence)>0.8:
		respuesta =(str(respuesta))
	else:
			respuesta = "No entendi, prueba otra vez"
	mensaje = open("respuesta.txt","w")
	mensaje.write(respuesta)
	mensaje.close()
	
# @autor Jose Jaime Rodriguez
# @param message recibir otro mensaje del usuario
# @fecha_creacion 16/04/2018
@bot.message_handler(func=lambda message:True)
def mensaje(message):
	bot_conversacional(message.text)
	respuesta = open("respuesta.txt","r")
	respuesta = respuesta.read()
	bot.reply_to(message, respuesta)
	
bot.polling()
