import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import logging

logger = logging.info
logger = print
delay = 5
button = Button.left
start_stop_key = KeyCode(char='a')
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        logger('start clicking')
        self.running = True

    def stop_clicking(self):
        logger('stop clicking')
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                logger('click')
                mouse.click(self.button)
                time.sleep(self.delay)

mouse = Controller()
click_thread = ClickMouse(delay=delay, button=button)
click_thread.start()


def on_press(key):
    logger(key)
    if key == start_stop_key:
        logger('hello')
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()