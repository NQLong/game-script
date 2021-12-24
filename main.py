from fishing import Fishing, FishingController, logger, start_stop_key, exit_key
from datetime import timedelta
from pynput.keyboard import Listener

fishing_thread = Fishing(delay=4, interval=0.2)
fishing_controller = FishingController(
    fishing_thread,
    delay=int(timedelta(minutes=5).total_seconds())
)

fishing_thread.start()
fishing_controller.start()


def on_press(key):
    logger(key)
    if key == start_stop_key:
        if fishing_controller.running:
            fishing_controller.stop_fishing()
        else:
            fishing_controller.start_fishing()
    elif key == exit_key:
        fishing_controller.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
