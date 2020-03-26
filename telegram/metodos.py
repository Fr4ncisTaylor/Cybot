import json
import requests
from . import config
import os

api = 'https://api.telegram.org/bot' # TELEGRAM API URL

class api(object):
    def __init__(self, token):
      self.token = token
      self.api   = api

    def request(self, method, js=None):
        r = requests.post(self.url+'/'+method, data=js)
        return json.loads(r.content.decode('utf8'))

    #### UPDATES ######
    def setWebhook(self, url, certificate=None,max_connections=None,allowed_updates=None):
        return request('setWebhook', locals())
    def getWebhook(self):
        return request('getWebhook', locals())
    def deleteWebhook(self):
        return request('deleteWebhook', locals())
    def getMe(self):
        return request('getMe', locals())
    def getUpdates(self,  allowed_updates = None,limit = None,offset = None,timeout = None) :
        return request(getUpdates, locals())
    ######### MESSAGE  #####
    def sendMessage(self, chat_id, text,parse_mode=None,disable_web_page_preview=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        return request('sendMessage', locals())
    def replyMessage(self, chat_id, text,disable_notification=None,disable_web_page_preview=None,parse_mode=None,reply_markup=None,reply_to_message_id=None) :
        return request('replyMessage', locals())
    def forwardMessage(self, chat_id, from_chat_id, message_id,disable_notification=None):
        return request('forwardMessage', locals())
    ######### STICKER
    def sendSticker(self, chat_id,sticker,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        return request('sendSticker', locals())
    ######### PHOTO
    def sendPhoto(self, chat_id,photo,caption=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        return request('sendPhoto', locals())
    ######### AUDIO
    def sendAudio(self, chat_id, audio,caption=None,duration=None,performer=None,title=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        return request('sendAudio', locals())
    ######### DOCUMENT
    def sendDocument(self, chat_id, document,caption=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        return request('sendDocument', locals())
    ######### VIDEO
    def sendVideo(self, chat_id, video,duration=None,width=None,height=None,caption=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        return request('sendVideo', locals())
    def sendVideoNote(self, chat_id, video_note,duration=None,length=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        return request('sendVideoNote', locals())
    ######### VOICE
    def sendVoice(self, chat_id, voice,caption=None,duration=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        return request('sendVideo', locals())
    ######### lOCATION
    def sendLocation(self, chat_id, latitude, longitude,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        return request('sendLocation', locals())
    ######### VENUE
    def sendVenue(self, chat_id, latitude, longitude,title,address,foursquare_id=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        return request('sendVenue', locals())
    ######### CONTACT
    def sendContact(self, chat_id, phone_number, first_name,last_name=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        return request('sendContact', locals())
    ######### CHAT ACTION
    def sendChatAction(self, chat_id, action):
        return request('sendChatAction', locals())
    #### PIN/UNPIN ####
    def pinChatMessage(self, chat_id, message_id,disable_notification=None):
        return request('pinChatMessage', locals())
    def unpinChatMessage(self, chat_id):
        return request('unpinChatMessage', locals())
    #### LEAVE
    def leaveChat(self, chat_id):
        return request('leaveChat', locals())
    #### GETS
    def getChat(self, chat_id):
        return request('getChat', locals())
    def getChatAdministrators(self, chat_id):
        return request('getChat', locals())
    def getChatMembersCount(self, chat_id):
        return request('getChatMembersCount', locals())
    def getChatMember(self, chat_id, user_id):
        return request('getChatMember', locals())
    ### BANHAMMER
    def kickChatMember(self, chat_id,user_id):
        return request('kickChatMember', locals())
    def unbanChatMember(self, chat_id,user_id):
        return request('unbanChatMember', locals())
    def restrictChatMember(self, chat_id,user_id,until_date=None,can_send_message=None,can_send_media_messages_=None,can_send_other_messages=None,can_add_web_page_previews=None):
        return request('restrictChatMember', locals())
    def promoteChatMember(self, chat_id,user_id,can_change_info=None,can_post_message=None,can_edit_messages=None,can_delete_messages=None,can_invite_users=None,can_restrict_members=None,can_pin_messages=None,can_promote_members=None):
        return request('promoteChatMember', locals())
    def exportChatInviteLink(self, chat_id):
        return request('exportChatInviteLink', locals())
    def setChatPhoto(self, chat_id,photo):
        return request('setChatPhoto', locals())
    def setChatTitle(self, chat_id,title):
        return request('setChatTitle', locals())
    def setChatDescription(self, chat_id,description):
        return request('setChatDescription', locals())
    #### EDITS
    def editMessageText(self, chat_id, message_id,text,inline_message_id=None,parse_mode=None,disable_web_page_preview=None,reply_markup=None):
        return request('editMessageText', locals())
    def editMessageCaption(self, caption,chat_id=None,message_id=None,inline_message_id=None,disable_web_page_preview=None,reply_markup=None):
        return request('editMessageCaption', locals())
    def editMessageReplyMarkup(self, text,chat_id=None,message_id=None,inline_message_id=None,parse_mode=None,disable_web_page_preview=None,reply_markup=None):
        return request('editMessageReplyMarkup', locals())
    #### DELETE
    def deleteMessage(self, chat_id,message_id):
        return request('deleteMessage', locals())
    def deleteChatPhoto(self, chat_id):
        return request('deleteChatPhoto', locals())
    #### GAME
    def sendGame(self, chat_id,game_short_name,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        return request('sendGame', locals())
    def setGameScore(self, user_id,score,force=None,disable_edit_message=None,chat_id=None,message_id=None,inline_message_id=None):
        return request('setGameScore', locals())
    def getGameHighScores(self, user_id,chat_id=None,message_id=None,inline_message_id=None):
        return request('getGameHighScores', locals())
    #### EXTRAS
    def run(self, arg):
        os.system('{}'.format(arg))