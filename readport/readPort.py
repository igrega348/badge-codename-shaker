from arduino import Arduino
import numpy as np

def run():
        
    filename = 'output12.txt'
    myArd = Arduino(filename)
    data = myArd.connect_arduino()
    
if __name__ == "__main__":
    run()
