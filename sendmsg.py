import readline, json, base64, time
from datetime import datetime
from getpass import getpass
from run import bcolors, printmsg
#password = getpass()
password = "testpass"
user="daiyu"
import cryptocode
'''
encoded = cryptocode.encrypt("mystring","mypassword")
## And then to decode it:
decoded = cryptocode.decrypt(encoded, "mypassword")
'''

while True:
    content=input("> ")
    # print(content)
    now=datetime.now().timestamp()
    encoded = cryptocode.encrypt(content,password)
    #print(encoded)
    #printmsg(now, user, content)
    with open("msg.json", "a") as f:
        f.write(json.dumps({"time":datetime.now().timestamp(), "user":user, 
        "content":encoded})+"\n")
