from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import urllib.request, json

# Bot Token
TOKEN = "503623178:AAFMYAa8JaF6SbB_8fVnhKnDOYi6lSiWds0"
# Test Kommandos
KOMMANDOS = ["/GETBTC", "/GETETH", "/GETXRP", "/GETLTC"]
NUMBEROFCOLUMNS = 2

def start(bot, update):
    keyboard = []
    for i in range(0, len(KOMMANDOS), NUMBEROFCOLUMNS):
        zeile = []
        j=0
        while((j < NUMBEROFCOLUMNS) and (i + j < len(KOMMANDOS))):
            zeile.append(KOMMANDOS[i+j])
            j = j + 1
        keyboard.append(zeile)
    update.message.reply_text('Herzlich Willkommen!', reply_markup = telegram.ReplyKeyboardMarkup(keyboard = keyboard))

#
# Command Optionen
#
def getBTC(bot, update):
    with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR") as url:
        data = json.loads(url.read().decode())
        bot.sendMessage(update.message.chat.id, data["EUR"])

def getETH(bot, update):
    with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR") as url:
        data = json.loads(url.read().decode())
        bot.sendMessage(update.message.chat.id, data["EUR"])

def getXRP(bot, update):
    with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR") as url:
        data = json.loads(url.read().decode())
        bot.sendMessage(update.message.chat.id, data["EUR"])

def getLTC(bot, update):
    with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,EUR") as url:
        data = json.loads(url.read().decode())
        bot.sendMessage(update.message.chat.id, data["EUR"])

#
# Initialisiere Bot und adde Commandhandler
#

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('getBTC', getBTC))
updater.dispatcher.add_handler(CommandHandler('getETH', getETH))
updater.dispatcher.add_handler(CommandHandler('getXRP', getXRP))
updater.dispatcher.add_handler(CommandHandler('getLTC', getLTC))

#
# Start
#

updater.start_polling()
updater.idle()


# JSON Zugriff auf Force Reply Nachricht
# update.message.reply_to_message