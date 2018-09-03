#! python3
#https://www.youtube.com/channel/UCsZs-p37pse_4UXG-alR47w   (My channel where I explain this code and demonstrate it working)
# clipboardToTxt.py - Pastes what you copy into a text file
import time
import pyperclip
from contextlib import redirect_stdout
clipboard = ''
while 1 != 2:
    time.sleep(.1) #with this checks ~10 times a second, without it checks ~600 times a second
    if clipboard != pyperclip.paste():
        clipboard = pyperclip.paste()
        with open('clipboard.txt', 'a') as f:
            with redirect_stdout(f):
                print(clipboard + '\n')




