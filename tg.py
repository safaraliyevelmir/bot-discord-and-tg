import telegram.ext
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from djinni import DjinniBot

def find_job(update, context):
    message = update.message.text
    ls = message.split(" ")   
    bot = DjinniBot() 
    for i in bot.job_features(ls[0]):
        if i.__iter__():
            for j in i[:5]:
                update.message.reply_text(bot.MAIN_URL+j)

def start(update,source):
    update.message.reply_text("Selam")
    
    
update = telegram.ext.Updater("6287333417:AAFQvVQCTdnU8aQDqUHX4U4lZZcpvdocyV0",use_context=True)
disp = update.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(MessageHandler(Filters.text, find_job))

update.start_polling()
update.idle()