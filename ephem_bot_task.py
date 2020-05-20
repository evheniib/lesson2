import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)


def greet_user(update, context):
    print ("Вызван /start")
    update.message.reply_text("Hello, is you my creator?")


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def planet_info (update, context):
    user_text = update.message.text.split()
    planet_dict = {
        "Mercury": ephem.Mercury('2000/01/01'), 
        "Venus": ephem.Venus('2000/01/01'), 
        "Mars": ephem.Mars('2000/01/01'), 
        "Jupiter": ephem.Jupiter('2000/01/01'), 
        "Saturn": ephem.Saturn('2000/01/01'), 
        "Uranus": ephem.Uranus('2000/01/01'), 
        "Neptune": ephem.Neptune('2000/01/01')
    }
    planet_names = list(planet_dict.keys())

    if len(user_text) == 2:
        word = user_text[1].capitalize()
        switcher = True
        for planet in planet_names:
            if word == planet:
                constellation = ephem.constellation(planet_dict[planet])
                update.message.reply_text(constellation)
                switcher = False
                break  
            elif word == "Earth":
                update.message.reply_text("Eath has no constellation")
                switcher = False
                break
        if switcher == True:
            update.message.reply_text("Wrong planet pls enter correct name of planet")
    else:
        update.message.reply_text("Wrong command. Pls type for example '/planet Mars'")

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")

    mybot.start_polling()

    mybot.idle()

if __name__ == "__main__":
    main()