_cols = 220
_rows = 50

keyboard.send_keys("SHELL=/bin/bash script -q /dev/null")
keyboard.send_keys("<enter>")
time.sleep(1)
keyboard.send_keys("<ctrl>+z")
time.sleep(0.5)

keyboard.send_keys('stty raw -echo')
keyboard.send_keys("<enter>")
time.sleep(0.5)

keyboard.send_keys('fg')
keyboard.send_keys("<enter>")
time.sleep(0.5)

keyboard.send_keys('fg')
keyboard.send_keys("<enter>")
keyboard.send_keys("<enter>")
time.sleep(0.5)

keyboard.send_keys('stty rows {} columns {}'.format(_rows,_cols))
keyboard.send_keys("<enter>")
time.sleep(0.5)

keyboard.send_keys('export TERM=xterm-256color')
keyboard.send_keys("<enter>")

