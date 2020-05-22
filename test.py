
while True:

    from pynput.keyboard import Key, Controller

    import random
    import time

    keyboard = Controller()

    ad1 = random.randint(1, 4)

    time.sleep(4)

    if ad1 == 1:
        keyboard.press("t")
        keyboard.release("t")
        time.sleep(1)
        keyboard.type("Do /join sagamines for a unique and fun mining experience")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        exit()

    if ad1 == 2:
        keyboard.press("t")
        keyboard.release("t")
        time.sleep(1)
        keyboard.type("Join sagamines just the best mh server ¯\_(ツ)_/¯")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        exit()

    if ad1 == 3:
        keyboard.press("t")
        keyboard.release("t")
        time.sleep(1)
        keyboard.type("Can't find a good server? I got you do /join sagamines")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        exit()

    if ad1 == 4:
        keyboard.press("t")
        keyboard.release("t")
        time.sleep(1)
        keyboard.type("Tired of boring servers? Join sagamines for a fun mining experience")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        exit()














