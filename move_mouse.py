#!/usr/bin/env python3

import pyautogui
from random import randrange
from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()
width, height= pyautogui.size()
interval = 60 # seconds to sleep after each movement of mouse pointer

# print detected screen resolution - information only
print("Detected screen resolution:", str(width) + 'x' + str(height))

def move_mouse(w, h, i):
	# get random coordinates for mouse
	wpos = randrange(0, w)
	hpos = randrange(0, h)
	
	# Set pointer position
	mouse.position = (wpos, hpos)

	# sleep for a minute
	sleep(i)

while True:
	move_mouse(width, height, interval)

