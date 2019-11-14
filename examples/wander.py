#!/usr/bin/python3
from sloth import Sloth
sloth = Sloth([1,2,3,4])
import random
from ezblock import delay

turn = None

sloth.set_offset([0,0,0,0])
turn = ['turn left', 'turn right', 'stop']


def forever():
  global turn
  sloth.do_action(turn[int(random.randint(0, 2) - 1)], (random.randint(2, 7)), 100)
  sloth.do_action('forward', (random.randint(4, 7)), 100)
  sloth.do_action('stop', 1, 100)
  delay((random.randint(3, 15) * 100))

if __name__ == "__main__":
    while True:
        forever()  