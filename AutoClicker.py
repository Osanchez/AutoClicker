import threading
import random
import time

import pynput
from pynput.mouse import Button, Controller as Mouse
from pynput.keyboard import Key, Controller as Keyboard
from DirectKeys import PressKey, ReleaseKey, Move,  W, A, S, D


class KeyboardListener:

    def __init__(self):
        self.toggle_key = Key.f4
        self.toggle = False
        self.clicker = None

    def on_release(self, key):

        if key == self.toggle_key:
            self.toggle = not self.toggle

        if self.toggle:
            print("Auto-clicker Enabled")
            if self.clicker is None:
                self.clicker = AutoClicker()
            else:
                self.clicker.restart()
        else:
            print("Auto-clicker Disabled")
            if self.clicker is not None:
                self.clicker.stop()

    def begin_listener(self):

        with pynput.keyboard.Listener (
                on_release=self.on_release) as listen:
            listen.join()


class AutoClicker(threading.Thread):

    def __init__(self):
        super(AutoClicker, self).__init__()
        self.__stop_event = threading.Event()
        self.start()

    def restart(self):
        self.__stop_event.clear()

    def run(self):
        while True:
            while not self.__stop_event.is_set():
                self.auto_clicker()

    def stop(self):
        self.__stop_event.set()

    def stopped(self):
        return self.__stop_event.is_set()

    @staticmethod
    def auto_clicker():
        mouse = Mouse()
        random_event = random.randint(1, 100)

        choices = ["left", "right", "up", "down"]

        if random_event > 98:
            choice = random.choice(choices)

            # Left Camera Movement
            if choice == "left":
                print("Left Movement")
                PressKey(A)
                time.sleep(0.1)
                ReleaseKey(A)
                PressKey(D)
                time.sleep(0.1)
                ReleaseKey(D)
                time.sleep(1)

            elif choice == "right":  # Right Camera Movement
                print("Right Movement")
                PressKey(D)
                time.sleep(0.1)
                ReleaseKey(D)
                PressKey(A)
                time.sleep(0.1)
                ReleaseKey(A)
                time.sleep(1)

            elif choice == "up":  # Right Camera Movement
                random_movement = random.randint(0, 10)
                Move(0, -random_movement)
                time.sleep(2)
                Move(0, random_movement)
                time.sleep(2)

            elif choice == "down":  # Right Camera Movement
                random_movement = random.randint(0, 10)
                Move(0, random_movement)
                time.sleep(2)
                Move(0, -random_movement)
                time.sleep(2)

        mouse.click(Button.right)  # Clicks the left mouse button once
        time.sleep(random.uniform(0.2, 0.3))


if __name__ == "__main__":
    listener = KeyboardListener()
    listener.begin_listener()
