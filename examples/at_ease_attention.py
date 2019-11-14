#!/usr/bin/python3
from sloth import Sloth
sloth = Sloth([1,2,3,4])
from ezblock import delay

AtEase = None
Attention = None

sloth.set_offset([0,0,0,0])
sloth.add_action("AtEase", [[(-45),0,(-20),0]])
AtEase = "AtEase"
sloth.add_action("Attention", [[(-10),0,10,0]])
Attention = "Attention"


def forever():
  global AtEase, Attention
  sloth.do_action(Attention, 1, 100)
  delay(5000)
  sloth.do_action(AtEase, 1, 100)
  delay(3000)

if __name__ == "__main__":
    while True:
        forever()  