# @autor(es) Jose Jaime Rodriguez
# @nombre_archivo botelegram
# @fecha 23/04/2018
# @descripción Programa de ejemplo sobre libreria de telebot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
	"Ejemplo Bot",
	trainer = "chatterbot.trainers.ChatterBotCorpusTrainer",
	storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
	database='LasMichesDeDany-database'
	)
	
#bot.train(
#	"chatterbot.corpus.spanish.greetings"
#	)

#conv = open('caso_1.txt', 'r').readlines()

#bot.set_trainer(ListTrainer)

#bot.train(conv)
print('Type something to begin...')


# @autor Jose Jaime && Oscar Lira
# @param 
# @fecha_creacion 23/04/2018
while True:
    try:
        request = input ('You :')
        response = bot.get_response(request)
        #print('Bot: ', response)
        if float (response.confidence)>0.8:
            print('Bot: ',response)
        else:
            print("No entendi, prueba otra vez")
        

   # @autor Alma Karen Jara Valencia
   # @param message interrupcion para salir del programa
   # @fecha_creacion 23/04/2018
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
