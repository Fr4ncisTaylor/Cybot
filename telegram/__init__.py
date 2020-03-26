# -*- coding: utf-8 -*-
import json
import os
import requests
from threading import Thread, local
from pprint import pprint
from . import metodos
import sys

api = 'https://api.telegram.org/bot' # TELEGRAM API URL
def request(bot, method, js=None):
	r = requests.post(api+bot+'/'+method, data=js)
	return json.loads(r.content.decode('utf8'))

class start(object):
	def __init__(self, token, webhook, log=True):
		if webhook.startswith('http')== False or type(webhook) == int:
			print('Invalid webhook url')
			return
		self.token = token
		os.system('clear')
		req = request(self.token,'setWebhook', {'url': webhook+'/webhook'})
		if log == True:
			print("Webhook: {}\nResult: {}\nResult: {}\nState: {}".format(webhook, req['result'], req['description'],req['ok']))

	#### UPDATES ######
	def setWebhook(url, certificate=None,max_connections=None,allowed_updates=None):
		return request(self.token,'setWebhook', locals())
	def getWebhook(self):
		return request(self.token,'getWebhook', locals())
	def deleteWebhook(self):
		return request(self.token,'deleteWebhook', locals())
	def getMe(self):
		return request(self.token,'getMe', locals())
	def getUpdates(self,  allowed_updates = None,limit = None,offset = None,timeout = None) :
		return request(self.token,getUpdates, locals())
	######### MESSAGE  #####
	def sendMessage(self, chat_id, text,parse_mode=None,disable_web_page_preview=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
		return request(self.token,'sendMessage', locals())
	def replyMessage(self, chat_id, text,disable_notification=None,disable_web_page_preview=None,parse_mode=None,reply_markup=None,reply_to_message_id=None) :
		return request(self.token,'replyMessage', locals())
	def forwardMessage(self, chat_id, from_chat_id, message_id,disable_notification=None):
		return request(self.token,'forwardMessage', locals())
	######### STICKER
	def sendSticker(self, chat_id,sticker,disable_notification=None,reply_to_message_id=None,reply_markup=None):
		return request(self.token,'sendSticker', locals())
	######### PHOTO
	def sendPhoto(self, chat_id,photo,caption=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
		return request(self.token,'sendPhoto', locals())
	######### AUDIO
	def sendAudio(self, chat_id, audio,caption=None,duration=None,performer=None,title=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
		return request(self.token,'sendAudio', locals())
	######### DOCUMENT
	def sendDocument(self, chat_id, document,caption=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
		return request(self.token,'sendDocument', locals())
	######### VIDEO
	def sendVideo(self, chat_id, video,duration=None,width=None,height=None,caption=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
		return request(self.token,'sendVideo', locals())
	def sendVideoNote(self, chat_id, video_note,duration=None,length=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
		return request(self.token,'sendVideoNote', locals())
	######### VOICE
	def sendVoice(self, chat_id, voice,caption=None,duration=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
		return request(self.token,'sendVideo', locals())
	######### lOCATION
	def sendLocation(self, chat_id, latitude, longitude,disable_notification=None,reply_to_message_id=None,reply_markup=None):
		return request(self.token,'sendLocation', locals())
	######### VENUE
	def sendVenue(self, chat_id, latitude, longitude,title,address,foursquare_id=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
		return request(self.token,'sendVenue', locals())
	######### CONTACT
	def sendContact(self, chat_id, phone_number, first_name,last_name=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
		return request(self.token,'sendContact', locals())
	######### CHAT ACTION
	def sendChatAction(self, chat_id, action):
		return request(self.token,'sendChatAction', locals())
	#### PIN/UNPIN ####
	def pinChatMessage(self, chat_id, message_id,disable_notification=None):
		return request(self.token,'pinChatMessage', locals())
	def unpinChatMessage(self, chat_id):
		return request(self.token,'unpinChatMessage', locals())
	#### LEAVE
	def leaveChat(self, chat_id):
		return request(self.token,'leaveChat', locals())
	#### GETS
	def getChat(self, chat_id):
		return request(self.token,'getChat', locals())
	def getChatAdministrators(self, chat_id):
			return request(self.token,'getChat', locals())
	def getChatMembersCount(self, chat_id):
		return request(self.token,'getChatMembersCount', locals())
	def getChatMember(self, chat_id, user_id):
		return request(self.token,'getChatMember', locals())
	### BANHAMMER
	def kickChatMember(self, chat_id,user_id):
		return request(self.token,'kickChatMember', locals())
	def unbanChatMember(self, chat_id,user_id):
		return request(self.token,'unbanChatMember', locals())
	def restrictChatMember(self, chat_id,user_id,until_date=None,can_send_message=None,can_send_media_messages_=None,can_send_other_messages=None,can_add_web_page_previews=None):
		return request(self.token,'restrictChatMember', locals())
	def promoteChatMember(self, chat_id,user_id,can_change_info=None,can_post_message=None,can_edit_messages=None,can_delete_messages=None,can_invite_users=None,can_restrict_members=None,can_pin_messages=None,can_promote_members=None):
		return request(self.token,'promoteChatMember', locals())
	def exportChatInviteLink(self, chat_id):
		return request(self.token,'exportChatInviteLink', locals())
	def setChatPhoto(self, chat_id,photo):
		return request(self.token,'setChatPhoto', locals())
	def setChatTitle(self, chat_id,title):
		return request(self.token,'setChatTitle', locals())
	def setChatDescription(self, chat_id,description):
		return request(self.token,'setChatDescription', locals())
	#### EDITS
	def editMessageText(self, chat_id, message_id,text,inline_message_id=None,parse_mode=None,disable_web_page_preview=None,reply_markup=None):
		return request(self.token,'editMessageText', locals())
	def editMessageCaption(self, caption,chat_id=None,message_id=None,inline_message_id=None,disable_web_page_preview=None,reply_markup=None):
		return request(self.token,'editMessageCaption', locals())
	def editMessageReplyMarkup(self, text,chat_id=None,message_id=None,inline_message_id=None,parse_mode=None,disable_web_page_preview=None,reply_markup=None):
		return request(self.token,'editMessageReplyMarkup', locals())
	#### DELETE
	def deleteMessage(self, chat_id,message_id):
		return request(self.token,'deleteMessage', locals())
	def deleteChatPhoto(self, chat_id):
		return request(self.token,'deleteChatPhoto', locals())
	#### GAME
	def sendGame(self, chat_id,game_short_name,disable_notification=None,reply_to_message_id=None,reply_markup=None):
		return request(self.token,'sendGame', locals())
	def setGameScore(self, user_id,score,force=None,disable_edit_message=None,chat_id=None,message_id=None,inline_message_id=None):
		return request(self.token,'setGameScore', locals())
	def getGameHighScores(self, user_id,chat_id=None,message_id=None,inline_message_id=None):
		return request(self.token,'getGameHighScores', locals())
	#### EXTRAS
	def run(self, arg):
		os.system('{}'.format(arg))
