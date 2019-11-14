#!/usr/bin/python3
from sloth import Sloth
sloth = Sloth([1,2,3,4])

sloth.set_offset([0,0,0,0])


def forever():
  sloth.do_action('moon walk left', 2, 100)
  sloth.do_action('moon walk right', 2, 100)
  sloth.do_action('turn right', 1, 100)
  sloth.do_action('shake left', 1, 100)
  sloth.do_action('turn left', 1, 100)
  sloth.do_action('shake right', 1, 100)
  sloth.do_action('go up and down', 1, 100)
  sloth.do_action('swing', 1, 100)
  sloth.do_action('big swing', 1, 100)
  sloth.do_action('stop', 1, 50)

if __name__ == "__main__":
    while True:
        forever()  