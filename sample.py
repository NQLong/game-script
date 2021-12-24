import pywinauto
import time
while True:
    print('click')
    pywinauto.mouse.click(button='left', coords=(800, 800)) 
    time.sleep(5)