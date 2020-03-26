from . import *
import requests,json
import time

print('-> Cybot Dual loop Starting...')
print('-> Mixing Whatsapp Control To Telegram painel...')
url = 'http://localhost:3000/webhook'
print('-> set webhook to localhost...')

def handler(msgs):
	print('-> Receive a message')
	print('-> Sending to cybot dual loop')
	msgs.update({'client': 'whatsapp'})
	req = requests.post(url, data=json.dumps(msgs))

def loop(chrome_path):
	print('-> Start chromedriver at "{}"'.format(chrome_path))
	print('-> Started\n___________________\n')
	wa_bot = Bot(chrome_path)
	wa_bot.loop(handler)