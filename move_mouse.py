#!/usr/bin/env python3

# vim: set expandtab:ts=2:sw=2

import sys
import argparse
import pyautogui
from random import randrange
from pynput.mouse import Button, Controller
from time import sleep
from time import time

mouse = Controller()
width, height= pyautogui.size() # compatibility issue with Apple Retina screen? Reports 1680x1050 instead of 2880×1800
interval = 60 # seconds to sleep after each movement of mouse pointer

# Argument parsing
parser = argparse.ArgumentParser(description="Arguments")
parser.add_argument("-e", "--expiry", help = "Expiry in minutes ; default is None", required=False, default=None, type=int)
parser.add_argument("-i", "--interval", help = "Frequency in minutes of mouse pointer moves ; default is 1 (every minute)", required=False, default=1, type=int)
args = parser.parse_args()

# Set expiry
if args.expiry is None:
	expiry = None
else:
	expiry = (args.expiry * 60)

# Set interval
if args.interval is None:
	interval = None
else:
	interval = (args.interval * 60)

# print detected screen resolution - information only
print("Detected screen resolution:", str(width) + 'x' + str(height))

def move_mouse(m, w, h, i, e):
	# get random coordinates for mouse
	wpos = randrange(0, w)
	hpos = randrange(0, h)
	
	# Set pointer position
	m.position = (wpos, hpos)

	# sleep for a minute
	sleep(i)

time_start = time()
if expiry is None:
	while True:
		move_mouse(mouse, width, height, interval, expiry)
else:
	try:
		while time() < time_start + expiry:
			move_mouse(mouse, width, height, interval, expiry)
	except:
		sys.exit(1)
