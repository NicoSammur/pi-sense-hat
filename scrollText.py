#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
red = (255, 0, 0)
sense.show_message("Text!", text_colour=red)
