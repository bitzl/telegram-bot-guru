import random

from telegram.ext import Updater, CommandHandler, MessageHandler

from facts import Facts

TELEGRAM_API_TOKEN = ''

FACTS = Facts.from_file('facts.yml')


def recommend_music(bot, update):
    fact = random.choice(FACTS.with_types(['music']))
    message = f'''Well, you look for music, young padawan? So it shall be:
    
    {fact.info}
    '''
    update.message.reply_text(message)


def guess_what_the_user_wants_to_know(bot, update):
    tags_of_interest = [tag for tag in FACTS.get_tags() if tag in update.message.text]
    fact = random.choice(FACTS.with_tags(tags_of_interest))
    message = f'''Well, for the path of your enlightenment, you have to look at:
    
    {fact.info}
    '''
    update.message.reply_text(message)


def main():
    updater = Updater(TELEGRAM_API_TOKEN)
    updater.dispatcher.add_handler(CommandHandler('music', recommend_music))
    updater.dispatcher.add_handler(MessageHandler(guess_what_the_user_wants_to_know))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
