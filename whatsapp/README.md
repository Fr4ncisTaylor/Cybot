### A simple example

```Python
import Cybot

bot = Cybot.Bot("path/to/chromedriver")

def handler(msg):
    print(msg)

bot.loop(handler)
```

<b>Let's supposewe send "Hi!" for our bot... the output wold be this:</b>

```python
{'ack': -1,
 'body': 'Hi!',
 'broadcast': False,
 'chat': {'id': '5513999999999@c.us',
          'image': {'eurl': 'https://pps.whatsapp.net/v/t61.24694-24/75492922_230397868138237_4419395424018435871_n.jpg?oe=5E7D0FA9&oh=d9d2f59b5887ef1de7987385e1c43196',
                    'full': 'https://web.whatsapp.com/pp?e=https%3A%2F%2Fpps.whatsapp.net%2Fv%2Ft61.24694-24%2F75492922_230397868138237_4419395424018435871_n.jpg%3Foe%3D5E7D0FA9%26oh%3Dd9d2f59b5887ef1de7987385e1c43196&t=l&u=5513988631138%40c.us&i=1584414884',
                    'img': 'https://web.whatsapp.com/pp?e=https%3A%2F%2Fpps.whatsapp.net%2Fv%2Ft61.24694-24%2F75492922_230397868138237_4419395424018435871_n.jpg%3Foe%3D5E7D0FA9%26oh%3Dd9d2f59b5887ef1de7987385e1c43196&t=s&u=5513988631138%40c.us&i=1584414884'},
          'isBusiness': False,
          'isEnterprise': False,
          'isMe': False,
          'isMyContact': True,
          'title': 'Francis Eu'},
 'isForwarded': False,
 'isGroup': False,
 'isReadOnly': False,
 'message': {'type': 'chat'},
 'star': False,
 'timestamp': 1584995122,
 'type': 'chat'}
```
* * *
* Send a message

```python
bot.sendMessage(chat_id, "Hello!")
```
