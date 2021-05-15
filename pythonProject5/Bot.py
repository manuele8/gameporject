from telegram.ext import Updater
updater = Updater(token = "1297291092:AAGYPz1MGBZd8_IiX4-JYjCmR_A7xP5_O6Y", use_context = True)
updater.start_polling()
print("bot avviato")
updater.idle()
