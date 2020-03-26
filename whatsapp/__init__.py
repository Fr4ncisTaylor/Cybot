import time
from .webwhatsapi import WhatsAPIDriver
from .webwhatsapi.objects.message import Message
from pprint import pprint
from . import helper

class Bot(object):
	def __init__(self, path):
		self.path = path
		driver = WhatsAPIDriver(executable_path=self.path)
		driver.wait_for_login()
		self.driver = driver
		
	def downloadFile(self, media_message):
		return self.driver.download_media(media_message)
	def sendMessage(self, chat_id, message):
		return self.driver.chat_send_message(chat_id, message)
	def sendMedia(self, chat_id, path, caption='a'):
		return self.driver.send_media(chatid=chat_id,path=path, caption=caption)
	def getMyContacts(self):
		return self.driver.get_my_contacts()
	def getAllChats(self):
		return self.driver.get_all_chats()
	def getAllChatId(self):
		return self.driver.get_all_chat_ids()
	def sendChatSeen(self, chat_id):
		return self.driver.chat_send_seen(chat_id)
	def getGroupParticipant(self, chat_id):
		return self.driver.group_get_participants_ids(chat_id)
	def getGroupParticipantNames(self, chat_id):
		return self.driver.group_get_participants(chat_id)
	def getAdminsId(self, chat_id):
		return self.driver.group_get_admin_ids(chat_id)
	def getGroupAdmins(self, chat_id):
		return self.driver.group_get_admins(chat_id)
	def getProfilePhoto(self, chat_id):
		return self.driver.get_profile_pic_from_id(chat_id)
	def battery(self):
		return self.driver.get_battery_level()
	def leaveChat(self, chat_id):
		return self.driver.leave_group(chat_id)
	def deleteChat(self, chat_id):
		return self.driver.delete_chat(chat_id)
	def deleteMessage(self, chat_id, message_array):
		return self.driver.delete_message(chat_id, message_array)
	def blockUser(self, chat_id):
		return self.driver.contact_block(chat_id)
	def unblockUser(self, chat_id):
		return self.driver.contact_unblock(chat_id)
	def banChatMember(self, chat_id, user_id):
		return self.driver.remove_participant_group(chat_id, user_id)
	def promoveParticipant(self, chat_id, user_id):
		return self.driver.promove_participant_admin_group(chat_id, user_id)
	def demoteParticipant(self, chat_id, user_id):
		return self.driver.demote_participant_admin_group(chat_id, user_id)
	
	def getContact(self, user_id):
		return self.driver.get_contact_from_id(user_id)
	def getChat(self, chat_id):
		return self.driver.get_chat_from_id(chat_id)
	def getChatForName(self, name):
		return self.driver.get_chat_from_name(name)
	def getChatFromPhone(self, phone):
		return self.driver.get_chat_from_phone_number(phone)
	
	def loop(self, handler):
		while True:
			time.sleep(3)
			for contact in self.driver.get_unread():
				for message in contact.messages:
					msg = message.get_js_obj()
					try:handler(msg, message)
					except:handler(msg)
