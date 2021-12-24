import win32api
import win32con
import time

import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import logging

logger = logging.info
logger = print
delay = 5
button = Button.left
start_stop_key = KeyCode(char=']')
exit_key = KeyCode(char='[')


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



class ClickMouse(threading.Thread):
    def __init__(self, delay, interval=1):
        super().__init__()
        self.delay = delay
        self.interval = interval
        self.running = False
        self.program_running = True

    def start_clicking(self):
        logger('start fishing')
        self.running = True

    def stop_clicking(self):
        logger('stop fishing')
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                logger('throw rod')
                click()
                time.sleep(self.delay)
                logger('catch')
                click()
                time.sleep(self.interval)



click_thread = ClickMouse(delay=4, interval=0.5)
click_thread.start()


def on_press(key):
    logger(key)
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()





