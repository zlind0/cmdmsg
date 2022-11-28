#!/usr/bin/env python3

import json, readline, time, base64
from datetime import datetime
import cryptocode
'''
encoded = cryptocode.encrypt("mystring","mypassword")
## And then to decode it:
decoded = cryptocode.decrypt(encoded, "mypassword")
'''
from getpass import getpass


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printmsg(t, name, content):
    print(f"{bcolors.OKGREEN}{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))}{bcolors.ENDC}  {bcolors.OKCYAN}{name}{bcolors.ENDC}\n{content}")

if __name__ == "__main__":
    #password = getpass()
    printed=set()
    password = "testpass"
    print(f"{bcolors.FAIL}ZHA JI's{bcolors.ENDC} secure chat server.")
    printmsg(datetime.now().timestamp(), "Hello", "You logged in")

    while True:
        with open('msg.json') as f:
            contents=f.readlines()
            for l in contents[-10:]:
                l=json.loads(l)
                if l['time'] not in printed:
                    #print(base64.b64decode(l['content'].encode('utf-8')))
                    printmsg(l['time'], l['user'], 
                        cryptocode.decrypt(l['content'], password))
                    printed.add(l['time'])
        time.sleep(1)
