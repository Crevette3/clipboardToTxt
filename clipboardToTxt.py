#! python3
#https://www.youtube.com/channel/UCsZs-p37pse_4UXG-alR47w   (My channel where I explain this code and demonstrate it working)
# clipboardToTxt.py - Pastes what you copy into a text filefrom 

import time
import sys
import pyperclip

last_paste = ''

while True:
    time.sleep(0.1)
    paste = pyperclip.paste().strip()
    if paste != last_paste:
        try:
            with open('clipboard.txt', 'a') as f:
                f.write('{}\n'.format(paste))
                last_paste = paste
        except Exception as e:
            sys.stderr.write("Error: {}".format(e))
            break
