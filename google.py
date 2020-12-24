import os, time

contents = clipboard.get_selection()

os.system("firefox --new-tab 'http://www.google.com'")
time.sleep(1.25)
keyboard.send_keys(contents)
time.sleep(0.25)
keyboard.send_keys("<enter>")
