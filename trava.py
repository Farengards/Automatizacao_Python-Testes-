import time as t
import pyautogui as py 

trava = 1000

py.moveTo(x=684, y=1048,duration=3)
t.sleep(2)
py.leftClick()
t.sleep(3)
py.moveTo(x=428, y=66,duration=3)

py.leftClick()
t.sleep(1)
py.write("https://web.whatsapp.com/")
py.press("enter")
t.sleep(6)

py.moveTo(x=365, y=516,duration=2)
py.leftClick()
py.moveTo(x=805, y=958,duration=2)
py.leftClick()
t.sleep(3)


for t in range (trava):
    py.hotkey("ctrl","v")
    py.press("enter")
    
    