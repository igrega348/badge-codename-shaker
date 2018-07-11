from arduinoStream import Arduino
from datetime import datetime
from analyseStream import loopScreen, initialiseDict

import numpy as np

def initialise():
#    filename = 'log.txt'
#    file = open(filename, mode='w')
   
    myArd = Arduino()
    return myArd
    
def screen(arduino):
    myArd = arduino
    dictIdent, dictVars = initialiseDict()
    a = datetime.now()
    b = datetime.now()
    dt = b - a
    while dt.seconds < 10:    
        try:
            b = datetime.now()
            dt = b-a
            data = myArd.readData()
#            data = str(data, 'utf-8')
            if data == None:
                pass
            else:
                data = str(data, 'utf-8')
                loopScreen(data, dictIdent, dictVars)
            
#            print(data)
        except KeyboardInterrupt:
            myArd.closePort()
            print(dictVars)
        except:
            myArd.closePort()

    for key in dictVars:
        dictVars[key] = np.array(dictVars[key], dtype = int)
    
#    print(dictVars)
    return dictVars

    
if __name__ == "__main__" :
    screen()


