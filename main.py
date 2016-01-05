'''
Created on Jan 4, 2016

@author: lorenzo
'''

"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats custom.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from custom import selectAnswer, selectPhoto
from telegram import Updater
import logging

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

def startHandler(bot, update):
    bot.sendMessage(update.message.chat_id, text='Porco Dio! Pronto a cagare il cazzo! (non funge ancora)')

def stopHandler(bot, update):
    bot.sendMessage(update.message.chat_id, text='Raga faccio come baglioni (non funziona ancora)')
    
    
def helpHandler(bot, update):
    bot.sendMessage(update.message.chat_id, text='Non rompere!')


def messageHandler(bot, update):
    ans = selectAnswer(update.message.text)
    if ans:
        bot.sendMessage(update.message.chat_id, ans)
    
    photo = selectPhoto(update.message.text)
    if photo:
        bot.sendPhoto(update.message.chat_id, photo)


def errorHandler(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("166865409:AAGSAEVXHyP1NlQaDOj65z4F9OgX5sarpGg")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("boz", startHandler)
    dp.addTelegramCommandHandler("muto", stopHandler)
    dp.addTelegramCommandHandler("help", helpHandler)

    # on noncommand i.e message - send a proper message on Telegram
    dp.addTelegramMessageHandler(messageHandler)

    # log all errors
    dp.addErrorHandler(errorHandler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()