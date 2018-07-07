from arduino-stream import Arduino
from datetime import datetime
from analyse-stream import loop, initialiseDict



def initialise():
    filename = 'log.txt'
    file = open(filename, mode='w')
    myArd = Arduino()
    
def run():
    initialise()
    a = datetime.now()
    b = datetime.now()
    dt = b - a
    while dt.seconds < 20:    
        try:
            b = datetime.now()
            dt = b-a
            data = myArd.readData()
            print(data)
        except KeyboardInterrupt:
            myArd.closePort()
    
    
        


