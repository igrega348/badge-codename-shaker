from arduino import Arduino
import numpy as np

filename = 'output6.txt'
myArd = Arduino(filename)
data = myArd.connect_arduino()


