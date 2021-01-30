#!/usr/bin/env python
"""
While otherwise good, LibreOffice writer is utter crap at pasting pictures, especially lots of pics at the same time
I went ahead and added the export as pdf part too

This program will:
ask for directory with pictures
ask for what name to give the output file
(assuming you have a blank LibreOffice writer doument open and click to it after prompts)
will paste all pictures in order of appearance in the folder
export it all as a pdf

Author: Anthony Alvarez
Date: 01/29/2021
"""

from pynput.keyboard import Key, Controller
from time import sleep
import os

# will simulate key presses
keyboard = Controller()

# presses multiple keys
def press_multiple(keys : list):
    global keyboard
    for i in keys:
        keyboard.press(i)

    # sleep(0.01)
    for i in keys:
        keyboard.release(i)

# ask for directory in which pics are
directory = "C:\\Users\\antho\\"
directory += input("Where are the pictures to export (assume already at C:\\Users\\antho)? ")
exported = input("What to export as? ")

"""
some documentation on what I need
keyboard.press(key) -> presses key
keyboard.release(key) -> releases key
keyboard.tap(key) -> press and release
keyboard.type(string) -> types a string
documentation on key
https://pythonhosted.org/pynput/keyboard.html#pynput.keyboard.Key


some custom settings in libre office writer I saved to make this easier
F4 -> export as pdf
crtl + A -> insert image
ctrl + W -> anchor as character
"""

# get the list of files in the directory
files = os.listdir(directory)
for filename in files:
    # wait a bit and retrieve filename
    sleep(0.5)
    name = f"\"{directory}\\{filename}\""

    # go to inset image
    press_multiple([Key.ctrl, "a"])
    
    # wait a bit and select the image
    sleep(0.5)
    keyboard.type(name)
    sleep(0.5)
    keyboard.tap(Key.enter)

    # wait a bit and anchor it as a character
    sleep(0.5)
    press_multiple([Key.ctrl, "w"])
    
    # wait a bit and advance to the next line
    sleep(0.5)
    for i in [Key.esc, Key.left, Key.enter]:
        keyboard.tap(i)
    
#export as pdf
sleep(0.5)
keyboard.tap(Key.f4)
sleep(0.1)
keyboard.tap(Key.enter)
sleep(1)
keyboard.tap(Key.backspace)
sleep(0.1)
keyboard.type(f"\"{directory}\{exported}.pdf\"")
keyboard.tap(Key.enter)
keyboard.tap(Key.enter)
