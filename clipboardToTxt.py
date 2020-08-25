#! python3
#https://www.youtube.com/channel/UCsZs-p37pse_4UXG-alR47w   (My channel where I explain this code and demonstrate it working)
# clipboardToTxt.py - Pastes what you copy into a text file

import time
import sys
import pyperclip

# Based on https://github.com/bolapara/clipboardToTxt pull request.

# By preloading last_paste with the existing clipboard we avoid saving
# something from the clipboard that was put there when this tool was not
# running.  That way you can safely kill it when copying a password and
# restart it afterwards and it will not steal your sensitive paste.
last_paste = pyperclip.paste().strip()

while True:
    time.sleep(0.1)
    paste = pyperclip.paste().strip()
    if paste != last_paste:
        try:
            with open('clipboard.txt', 'a',encoding="utf-8") as f:
                f.write('{}\n$\n'.format(paste))
                last_paste = paste
        except Exception as e:
            sys.stderr.write("Error: {}".format(e))
            break



