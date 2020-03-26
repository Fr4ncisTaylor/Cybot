# -*- coding:utf-8 -*-
import requests, json

__version__='1.0'

def Keyboard(**kwargs):
	return kwargs

class _bot(object):
	def __init__(self, acess_token, version=2.6):
		self.acess_token  = acess_token
		self.version      = version
		
class Bot(_bot):
	def __init__(self, acess_token, version=2.6):
		super(Bot, self).__init__(acess_token, version)
		self.acess_token = acess_token
		self.version     = version
		self.api         = "https://graph.facebook.com/v2.6/me/messages?access_token="+self.acess_token
		self.regular     = "REGULAR"
		self.silent_push = "SILENT_PUSH"
		self.no_push 	 = "NO_PUSH"

	def sendFacebook(self, payload):
		req = requests.post(self.api, json=payload)
		result = req.json()
		return result

	def sendMessage(self, recipient_id, message, button=None):
		if button == None:
			payload ={"recipient":{"id":recipient_id},"message":{"text":message}} 
			return self.sendFacebook(payload)
		else:
			payload = {
			  "recipient":{"id":recipient_id},
			  "message"  :{
			    "attachment":{
			      "type":"template",
			      "payload":{
			        "template_type":"button",
			        "text":message,
			        "buttons":button
			      		}}}}
			return self.sendFacebook(payload)

	def send_arquivs(self, recipient_id, url, file_type):
		payload = {"recipient":{
				"id":recipient_id},
				"message":{"attachment":{"type":file_type,"payload":{
				"url":"https://i.imgur.com/ttlb9aj.jpg","is_reusable":True}}}}
		payload = dict(recipient=dict(id=recipient_id), dict(message=dict(attachment=dict(type=file_type, payload=dict(url=url, is_reusable=True)))))
		return self.sendFacebook(payload)

	def sendImage(self, recipient_id, photo):
		return self.send_arquivs(recipient_id=recipient_id, url=photo, file_type='image')

	def sendVideo(self, recipient_id, video):
		return self.send_arquivs(recipient_id=recipient_id, url=video, file_type='video')

	def sendFile(self, recipient_id, file):
		return self.send_arquivs(recipient_id=recipient_id, url=file, file_type='file')

	def sendAudio(self, recipient_id, audio):
		return self.send_arquivs(recipient_id=recipient_id, url=audio, file_type='audio')


