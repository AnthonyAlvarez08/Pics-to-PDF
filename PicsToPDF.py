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
Date: 02/16/2021
"""

from pynput.keyboard import Key, Controller
from time import sleep
import os

# will simulate key presses
keyboard = Controller()
TIME = 0.5

# presses multiple keys
def press_multiple(keys : list):
    global keyboard
    for i in keys:
        keyboard.press(i)
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

files.sort() # sort normally
files.sort(key=lambda x: len(x)) # sort by length to aboid 1 10 2 placements

for filename in files:
    # wait a bit and retrieve filename
    sleep(TIME)
    name = f"\"{directory}\\{filename}\""

    # insert image
    press_multiple([Key.ctrl, "a"])
    
    # wait a bit and select the image
    sleep(TIME)
    keyboard.tap(Key.backspace)
    sleep(TIME)
    keyboard.type(name)
    sleep(TIME)
    keyboard.tap(Key.enter)

    # wait a bit and anchor it as a character
    sleep(TIME)
    press_multiple([Key.ctrl, "w"])
    
    # wait a bit and advance to the next line
    sleep(TIME)
    for i in [Key.esc, Key.left, Key.enter]: # maybe Key.down
        keyboard.tap(i)
        sleep(0.15)
    keyboard.press(Key.page_down)
    sleep(TIME)
    
    keyboard.release(Key.page_down)
    
#export as pdf
sleep(TIME)
keyboard.tap(Key.f4)
sleep(0.1)
keyboard.tap(Key.enter)
sleep(1)
keyboard.tap(Key.backspace)
sleep(TIME)
keyboard.type(f"\"{directory}\{exported}.pdf\"")
keyboard.tap(Key.enter)
keyboard.tap(Key.enter)
