import win32api
import win32con
import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import (
    Listener, 
    KeyCode, 
    Key, 
    Controller as KeyboardController
)

logger = print
delay = 5
button = Button.left
start_stop_key = KeyCode(char=']')
exit_key = KeyCode(char='[')

keyboard_controller = KeyboardController()

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.3)


def press(key):
    key= str(key)
    keyboard_controller.press(key)
    time.sleep(0.3)
    keyboard_controller.release(key)
    time.sleep(0.3)

