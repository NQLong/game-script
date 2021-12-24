from .common import press, click, logger
import threading
import time
from .fishing import Fishing

class FishingController(threading.Thread):
    POTION = [1, 2, 3, 4, 5]
    CHUM = 9

    def __init__(self, fishing_thread: Fishing, delay):
        self.fishing_thread = fishing_thread
        self.delay = delay
        self.program_running = True
        self.running = False
        super().__init__()

    def start_fishing(self):
        logger('start potion')
        self.running = True

    def stop_fishing(self):
        logger('stop potion')
        self.running = False

    def exit(self):
        self.fishing_thread.exit()
        self.stop_fishing()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                self.fishing_thread.stop_clicking()
                logger('drinking potion')
                click()
                for potion in self.POTION:
                    self.drink_potion(potion)
                logger('throwing chum')
                self.throw_chum()
                self.fishing_thread.start_clicking()
                time.sleep(self.delay)

    def drink_potion(self, number):
        logger('drinking potion {}'.format(number))
        press(number)
        click()
        time.sleep(1)

    def throw_chum(self):
        logger('throwing chum')
        press(self.CHUM)
        click()
        click()
        click()
        click()