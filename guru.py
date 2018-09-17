import random

import click
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from facts import Facts

FACTS = Facts.from_file('facts.yml')


def recommend_music(bot, update):
    music_facts = FACTS.with_types(['music'])
    if music_facts.is_empty():
        info = 'Listen to the music inside you…'
    else:
        fact = music_facts.random()
        info = fact.info
    message = f'''Well, you look for music young padawan? So it shall be:
        
    {info}
    '''
    update.message.reply_text(message, parse_mode='Markdown')


def guess_what_the_user_wants_to_know(bot, update):
    tags_of_interest = [tag for tag in FACTS.get_tags() if tag in update.message.text]
    facts = FACTS.with_tags(tags_of_interest)
    if facts.is_empty():
        message = f'Well, for the path of your enlightenment, you have to look inside yourself…'
    else:
        fact = facts.random()
        message = f'''Well, for the path of your enlightenment, you have to look at:
        
{fact.info}
'''
    update.message.reply_text(message, parse_mode='Markdown')


def print_errors(_, __, error):
    print(error)


@click.command()
@click.argument('telegram_api_token')
def main(telegram_api_token):
    updater = Updater(telegram_api_token)
    updater.dispatcher.add_handler(CommandHandler('music', recommend_music))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, guess_what_the_user_wants_to_know))
    updater.dispatcher.add_error_handler(print_errors)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
