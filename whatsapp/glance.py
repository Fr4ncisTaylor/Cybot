def simplify(msg):
	msg_type  = msg['type']
	if msg_type == 'chat':
		msg_type = 'message'
	elif msg_type == 'group':
		msg_type = 'message'
	elif msg_type == 'gp2':
		msg_type = 'message'
	elif msg_type == 'new_conversation':
		msg_type = 'new_conversation'
	elif msg_type== 'remove':
		msg_type = 'remove'
	elif msg_type == 'add':
		msg_type = 'add'
	else:
		msg_type = 'media'
	chat_id   = msg['chat']['id']
	timestamp = msg['timestamp']

	return chat_id, msg_type, timestamp
