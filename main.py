from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url
def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url
def get_doggo(update, context):
    url = get_image_url()
    c_id = update.message.chat_id
    context.bot.send_photo(chat_id=c_id, photo=url)

def main():
    updater = Updater('1340791035:AAH6iHwNKA_KSUxpy7pIVStAq2YCd4goRaM', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('get_doggo',get_doggo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
