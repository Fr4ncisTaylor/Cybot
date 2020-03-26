from .flask import Flask, request
from pprint import pprint
import json
import os
import time
import sys

class run(object):
	def __init__(self, handler, port=3000, debug=True, host='localhost', extra=False):
		self.handler = handler
		if type(handler) is dict:
			if 'message' not in handler:
				print('Handler require "message" argument for send api returns.')
				sys.exit()
		app = Flask(__name__)
		@app.route('/webhook', methods=['GET', 'POST'])
		def amanda():
			msgs = json.loads(request.data.decode())
			if msgs.get('message', None) is not None :
				msg = msgs['message']
				mtp = 'message'
				content_type = 'text'
			elif msgs.get('edited_message', None) is not None :
				mtp = 'edited_message'
				msg = msgs['edited_message']
			elif msgs.get('channel_post', None) is not None :
				msg = msgs['channel_post']
				mtp = 'channel_post'
			elif msgs.get('edited_channel_post', None) is not None :
				msg = msgs['edited_channel_post']
				mtp = 'edited_channel_post'
			elif msgs.get('inline_query', None) is not None :
				msg = msgs['inline_query']
				mtp = 'inline_query'
			elif msgs.get('chosen_inline_result', None) is not None :
				msg = msgs['chosen_inline_result']
				mtp = 'chosen_inline_result'
			elif msgs.get('callback_query', None) is not None :
				msg = msgs['callback_query']
				mtp = 'callback_query'
			elif msgs.get('shipping_query', None) is not None :
				msg = msgs['shipping_query']
				mtp = 'shipping_query'
			elif msgs.get('pre_checkout_query', None) is not None :
				msg = msgs['pre_checkout_query']
				mtp = 'pre_checkout_query'
			else:
				return ' ok', 200
			if (time.time() - msg['date']) > 999:
				return ' ok', 200
			if type(handler) is dict:
				if mtp in handler:
					handler[mtp](msg)
				else:
					if mtp == 'edited_message':
						handler['message'](msg)
					elif mtp == 'channel_post':
						try:handler['message'](msg)
						except:pass
					elif mtp == 'edited_channel_post':
						try:handler['message'](msg)
						except:pass
					elif mtp == 'callback_query':
						try:handler['callback_query'](msg)
						except:pass
					else:
						print('Warning: dont have "{}" in handler!!!'.format(mtp))
			else:
				handler(msg)
			return ' ok', 200
		print("Cybot start!")
		app.run(debug=debug, port=port, host=host)