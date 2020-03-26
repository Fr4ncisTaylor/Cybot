# -*- coding: utf-8 -*-
import json

def data(msg):
    return msg['data']

def identifier(msg):
    chat_id = msg['message']['chat']['id']
    msg_id = msg['message']['message_id']
    return {'chat_id' : chat_id,'msg_id' : msg_id}

def inline_keyboard(self):
    keyboard = {}
    ia = []

    for i in self:
        ia.append(i)

    keyboard['inline_keyboard'] = ia
    return json.dumps(keyboard)