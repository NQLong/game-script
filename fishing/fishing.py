import threading
from .common import click, logger, press
import time

class Fishing(threading.Thread):
    ROD = 0

    def __init__(self, delay, interval=1):
        super().__init__()
        self.delay = delay
        self.interval = interval
        self.running = False
        self.program_running = True

    def start_clicking(self):
        logger('start fishing')
        press(self.ROD)
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
