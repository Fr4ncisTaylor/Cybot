# -*- coding:utf-8 -*-
import platform,os, sys, pyfiglet, math, redis, time, datetime, traceback, json
from pprint import pprint
import requests, json

def dumps(**args):
	return json.dumps(args)

def makedict(**kwargs):
	return kwargs

def get_sys():
	os = platform.system()
	return os

########[ limpa o terminal ]
def clear():
	if get_sys() == 'Linux':
		clear = 'clear'
	if get_sys() == 'Windows':
		clear = 'cls'
	os.system(clear)

def list_dir(a):
	if get_sys() == 'Linux':
		lists = 'ls'
	if get_sys() == 'Windows':
		lists = 'dir'
	return os.system('%s %s' %(lists, a))

########[ encerra o sistema ]
def exit():
	sys.exit()

########[ faz um banner figlet ]
def figlet(text, font='doom'):
	f = pyfiglet.Figlet(font=font)
	return f.renderText(text)

########[ transforma bytes ]
def convert(size_bytes):
	if size_bytes == 0:
		return "0B"
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return "%s %s" % (s, size_name[i])

## [ VERIFY HAVE STR ITEM]
def get_str(string):
	if 'a' in string:
		return True
	if 'b' in string:
		return True
	if 'c' in string:
		return True
	if 'd' in string:
		return True
	if 'e' in string:
		return True
	if 'f' in string:
		return True
	if 'g' in string:
		return True
	if 'h' in string:
		return True
	if 'i' in string:
		return True
	if 'j' in string:
		return True
	if 'k' in string:
		return True
	if 'l' in string:
		return True
	if 'm' in string:
		return True
	if 'n' in string:
		return True
	if 'o' in string:
		return True
	if 'p' in string:
		return True
	if 'q' in string:
		return True
	if 'r' in string:
		return True
	if 's' in string:
		return True
	if 't' in string:
		return True
	if 'u' in string:
		return True
	if 'v' in string:
		return True
	if 'w' in string:
		return True
	if 'x' in string:
		return True
	if 'y' in string:
		return True
	if 'z' in string:
		return True
	else:
		return False

## [ VERIFY HAVE INT ITEM]
def get_int(ints):

	if '0' in ints:
		return True
	if '1' in ints:
		return True
	if '2' in ints:
		return True
	if '3' in ints:
		return True
	if '4' in ints:
		return True
	if '5' in ints:
		return True
	if '6' in ints:
		return True
	if '7' in ints:
		return True
	if '8' in ints:
		return True
	if '9' in ints:
		return True
	else:
		return False

########[ CALENDARIO ]
class data:
	datas = datetime.datetime.now()

	dia   = datas.day

	mes   = datas.month

	ano	  = datas.year

	hor  = datas.hour

	segundo = datas.second

	minuto = datas.minute

	hora = '{}:{}:{}'.format(hor, minuto, segundo)
	data = "{}/{}/{}".format(dia,mes,ano)
	datetime = {'time': hora, 'date': data}

##########[ reboot sys]
def reboot(sleep=2):
	time.sleep(2)
	os.execl(sys.executable, sys.executable, *sys.argv)

## [ COLOR LETRAS]
class cor:
	black   = '\033[900m'
	red     = '\033[901m'
	green   = '\033[902m'
	yellow  = '\033[903m'
	blue    = '\033[904m'
	magenta = '\033[905m'
	cyan    = '\033[906m'
	white   = '\033[907m'
