import os
import telegram
import random
from telegram.ext import MessageHandler, Filters, CommandHandler

TOKEN = os.environ.get('TOKEN')
PORT = int(os.environ.get('PORT', '8443'))
VERSION = 1.30
story = "C'era una volta 📖 una principessa 👸🏼 di nome Camilla, che viveva in un enorme castello 🏰 di ghiaccio ❄.\nCamilla aveva un pinguino 🐧 di nome Pingu e Camilla e Pingu erano molto amici 😊: tutti i giorni uscivano dal castello e giocavano a tirare le palle di neve ☃ ai passanti.\nNel castello viveva anche Chicco, un coniglio 🐰 che si divertiva a fare dolci 🍪 per Camilla e Pingu.\nUn giorno, mentre giocavano, presero in testa con una palla di neve la strega 🧙🏻‍♀️ Alberta, la quale si adirò profondamente 😡.\nChicco tentò di offrirle un dolce 🎂 per scusarsi 😥, ma la strega lo trasformò in un robottino 🤖 con la pancia a forma di sandwich 🥪.\nPingu si arrabbiò moltissimo 😤 per questo e la minacciò che se non avesse ri-trasformato chicco in un coniglio, avrebbe chiamato l'orco 👹 Parisi.\nLa strega senza paura gli disse di chiamarlo pure e quando l'orco Parisi arrivò, caricò in spalla Camilla e Pingu, e mentre lui conciava 🤕 per bene la strega, loro la prendevano a palle di neve e Chicco tirava sorbetti 🍧 al limone 🍋.\nLa strega scappò urlando 😱 e trasformò di nuovo Chicco in un coniglio.\nLa strega non tornò mai più al castello di Camilla e tutti vissero felici e contenti 🎈."
updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
random.seed()
#print("Ready.")

def processText(update, context):
	txt = update.message.text
	if txt.lower() == "moneta":
		moneta(update, context)
	elif ("e invece" in txt.lower()) or ("eh invece" in txt.lower()):
		context.bot.send_message(chat_id=update.message.chat_id, text="🐶")
	elif (txt.lower() == "saluto") or (txt.lower() == "saluta") or ("ciao" in txt.lower()) or ("piru" in txt.lower()) or ("pirù" in txt.lower()):
		saluto(update, context)
	elif txt.lower() == "camilla":
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text=story)
	else:
		try:
			whitelist = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZàÀáÁèÈéÉìÌíÍòÒóÓùÙúÚ\n\t")
			txt = "".join(filter(whitelist.__contains__, txt))
			w = txt.lower().split()
			d = []
			c = ["cau", "clau"]
			l = ["luli", "luly"]
			e = ["lisa", "ligi"]
			k = ["denis", "denny", "denni"]
			for el in c:
				for i in range(0, len(w)):
					if el in w[i]:
						d.append((i, "🧜🏻‍♀️"))
			for el in l:
				for i in range(0, len(w)):
					if el in w[i]:
						d.append((i, "👨🏻‍🚀"))
			for el in e:
				for i in range(0, len(w)):
					if el in w[i]:
						d.append((i, "🦄"))
			for el in k:
				for i in range(0, len(w)):
					if el in w[i]:
						d.append((i, "😱"))
			o = {"lu": "👨🏻‍🚀", "lù": "👨🏻‍🚀", "luca": "👨🏻‍🚀", "mine": "🐧", "ino": "🐶", "chicco": "🐰", "tlai": "🦊", "mee": "🦊", "zelena": "🍃", "byron": "🐶", "eli": "🦄"}
			for i in range(0, len(w)):
				if w[i] in o:
					d.append((i, o[w[i]]))
			if len(d) > 0:
				h = sorted(d, key=lambda item: item[0])
				t = ""
				for i in range(0, len(h)):
					t += h[i][1]
				context.bot.send_message(chat_id=update.message.chat_id, text=t)
		except:
			pass

def moneta(update, context):
	emoji = "🎬🥁💸💁🏻☁ - "
	if random.randint(0, 1) == 1:
		toss = "Testa"
	else:
		toss = "Croce"
	context.bot.send_message(chat_id=update.message.chat_id, text=emoji+toss)

def saluto(update, context):
	l1 = ["Piruuu!", "Piru piruuuu!", "Piru piii!", "Piru! 🐧", "Piruuuuuuuuu!"]
	context.bot.send_message(chat_id=update.message.chat_id, text=l1[random.randint(0, 4)])

def info(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text="CausBot - Versione {0}\n\nBy Luca Invernizzi, @Looka13\n\nBot realizzato in Python attraverso le librerie [python-telegram-bot](https://python-telegram-bot.org/) e in host su [Heroku](https://www.heroku.com/).".format(VERSION), parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)

def numero(update, context):
	t = "Formato da utilizzare:\n\n/numero a b\n\nCon a e b numeri interi relativi tali che a < b."
	if len(context.args) > 1:
		try:
			a = int(context.args[0])
			b = int(context.args[1])
			t = random.randint(a, b)
		except:
			pass
	context.bot.send_message(chat_id=update.message.chat_id, text=t)

# add handlers
msg_handler = MessageHandler(Filters.text, processText)
dispatcher.add_handler(msg_handler)
moneta_handler = CommandHandler("moneta", moneta)
dispatcher.add_handler(moneta_handler)
saluto_handler = CommandHandler("saluto", saluto)
dispatcher.add_handler(saluto_handler)
info_handler = CommandHandler("info", info)
dispatcher.add_handler(info_handler)
numero_handler = CommandHandler("numero", numero)
dispatcher.add_handler(numero_handler)

updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
#updater.bot.set_webhook("https://causbot.herokuapp.com/"+TOKEN)
updater.idle()