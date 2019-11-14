#!/usr/bin/python3
from sloth import Sloth
sloth = Sloth([1,2,3,4])
from ezblock import Pin
from ezblock import Ultrasonic

distance = None
reference = None

sloth.set_offset([0,0,0,0])
reference = 10

pin_D0=Pin("D0")

pin_D1=Pin("D1")


def forever():
  global distance, reference
  distance = Ultrasonic(pin_D0, pin_D1).read()
  if distance >= reference:
    sloth.do_action('forward', 1, 100)
  else:
    sloth.do_action('backward', 1, 100)
    sloth.do_action('stop', 1, 100)
    sloth.do_action('turn right', 2, 100)
    sloth.do_action('stop', 1, 100)

if __name__ == "__main__":
    while True:
        forever()
