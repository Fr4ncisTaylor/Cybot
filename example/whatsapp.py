# simple skeleto


from Cybot import whatsapp

bot = whatsapp.Bot('/home/taylor/chromedriver')

def handler(msg):
	pprint(msg)

bot.loop(handler)
