
from Cybot import telegram, whatsapp
from Cybot.telegram import loop
from pprint import pprint

webhook = "Webhook_URL"
token   = 'telegram_bot_token'
bot     = telegram.start(token, webhook)

def hanler(msg):
	pprint(msg)
  
telegram.loop.run(handler, debug=True)
