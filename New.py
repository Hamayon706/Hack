#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To MR-SH4DOW
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\33[%s;1m'%str(31+j))
    x += '\33[0m'
    x = x.replace('!0','\33[0m')
    sys.stdout.write(x+'\')


def jalan(z):
	for e in z + '\':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\33[1;97m[+] Token :")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\33[1;91m[!] Wrong"
		e = raw_input("\33[1;91m[?] \33[1;92mWant to pick up token?\33[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		menu()

def phone():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')		

#Dev:MR-SH4DOW-ALONE
##### LOGO #####
logo = """

\33[1;91m ░█████╗░███████╗███████╗██╗░█████╗░██╗░█████╗░██╗░░░░░
\33[1;92m ██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║██╔══██╗██║░░░░░
\33[1;94m ██║░░██║█████╗░░█████╗░░██║██║░░╚═╝██║███████║██║░░░░░
\33[1;97m ██║░░██║██╔══╝░░██╔══╝░░██║██║░░██╗██║██╔══██║██║░░░░░
\33[1;93m ╚█████╔╝██║░░░░░██║░░░░░██║╚█████╔╝██║██║░░██║███████╗
\33[1;95m ░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝╚══════╝

\33[1;91m
░█████╗░███████╗███████╗██╗░█████╗░██╗░█████╗░██╗░░░░░
██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║██╔══██╗██║░░░░░
██║░░██║█████╗░░█████╗░░██║██║░░╚═╝██║███████║██║░░░░░
██║░░██║██╔══╝░░██╔══╝░░██║██║░░██╗██║██╔══██║██║░░░░░
 ╚█████╔╝██║░░░░░██║░░░░░██║╚█████╔╝██║██║░░██║███████╗
░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝╚══════╝
                                                   

\33[1;91m•───────────────────────────────────────────•
\33[1;97m•-----------------\33[1;37mALI-OFFICAL_AL1\33[1;97m-----------------•
 \33[1;97m•▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
\33[1;41m\33[1;37m[⚡🔥\33[1;37mAuthor Name: MR-0FIICAL-ALI🔥⚡\33[1;37m]\33[1;0m
\33[1;41m\33[1;37m[⚡🔥\33[1;37m☏ →+923063112*** 🔥⚡\33[1;37m]\33[1;0m
\33[1;41m\33[1;37m[⚡🔥\33[1;37mYT Channel:TECHNICAL ALI 786🔥⚡\33[1;37m]\33[1;0m
\33[1;41m\33[1;37m[⚡🔥 \33[1;37mFACEBOOK ID: OFFICAL-ALI 🔥⚡\33[1;37m]\33[1;0m
\33[1;97m•▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
\33[1;97m•-----------------\33[1;37mMR-ALI-OFFICAL\33[1;97m-----------------•
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\\1b[1;93mALI-OFFICAL█████████████████▒▒▒▒▒▒▒▒..99% \1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\33[31mNot Vuln"
vuln = "\33[32mVuln"

os.system("clear")
print  """
\33[1;91m───▄▀▀▀▀▀───▄█▀▀▀█▄
\33[1;92m──▐▄▄▄▄▄▄▄▄██▌▀▄▀▐██
\33[1;93m──▐▒▒▒▒▒▒▒▒███▌▀▐███
\33[1;94m───▌▒▓▒▒▒▒▓▒██▌▀▐██
\33[1;95m───▌▓▐▀▀▀▀▌▓─▀▀▀▀▀  
\33[1;97m•▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
\33[1;97m•───────────────────────────────────────────•
\33[1;91m─────█─▄▀█──█▀▄─█─────\33[1;97m─────█─▄▀█──█▀▄─█───── 
\33[1;91m────▐▌──────────▐▌────\33[1;97m────▐▌──────────▐▌────
\33[1;91m────█▌▀▄──▄▄──▄▀▐█────\33[1;97m────█▌▀▄──▄▄──▄▀▐█────
\33[1;91m───▐██──▀▀──▀▀──██▌───\33[1;97m───▐██──▀▀──▀▀──██▌───
\33[1;91m──▄████▄──▐▌──▄████▄──\33[1;97m──▄████▄──▐▌──▄████▄──    
\33[1;97m$$\ $$\ $$ | $$ | $$ | $$ | $$$$$$\ $$$$$$\$$$$\ $$$$$$\ $$\ $$\ $$$$$$\ $$$$$$$\ $$$$$$$$ | \____$$\ $$ _$$ _$$\ \____$$\ $$ | $$ |$$ __$$\ $$ __$$\ $$ __$$ | $$$$$$$ |$$ / $$ / $$ | $$$$$$$ |$$ | $$ |$$ / $$ |$$ | $$ | $$ | $$ |$$ __$$ |$$ | $$ | $$ |$$ __$$ |$$ | $$ |$$ | $$ |$$ | $$ | $$ | $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$ |$$ | $$ | \__| \__| \_______|\__| \__| \__| \_______| \____$$ | \______/ \__| \__| $$\ $$ | \$$$$$$ | \______/
