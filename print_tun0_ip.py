import os
with open('/home/bob/git/autokey/host.txt') as file: 
    ip = file.read().replace('\n', '')

keyboard.send_keys("%s" % ip)
