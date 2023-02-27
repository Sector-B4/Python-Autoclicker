import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode


# Use to toggle the Autoclick ON/OFF
# Swap "x" to any key you want
toggleKey = KeyCode(char="x")

active = False
mouse = Controller()

def clicker():
    while True:
        if active:
            mouse.click(Button.left, 1)
        """
        WARNING: Do not remove time.sleep() and itxs value or yxou won't
        be able to toggle it off and might crash your pc. it should
        always have a value even if its 0
        """
        time.sleep(0.0) # 0.001 = 70 CPM | 0 = idk it crashed the website
def togglegEvent(key):
    if key == toggleKey:
        global active
        active = not active

clickThread = threading.Thread(target=clicker)
clickThread.start()

with Listener(on_press=togglegEvent) as listener:
    listener.join()