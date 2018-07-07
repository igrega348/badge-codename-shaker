from arduinoStream import Arduino
from datetime import datetime
from analyseStream import loop, initialiseDict



def initialise():
#    filename = 'log.txt'
#    file = open(filename, mode='w')
   
    myArd = Arduino()
    return myArd
    
def run():
    myArd = initialise()
    dictIdent, dictVars = initialiseDict()
    a = datetime.now()
    b = datetime.now()
    dt = b - a
    while dt.seconds < 10:    
        try:
            b = datetime.now()
            dt = b-a
            data = myArd.readData()
            data = str(data, 'utf-8')
            if data == None:
                pass
            else:
                loop(data, dictIdent, dictVars)
            
#            print(data)
        except KeyboardInterrupt:
            myArd.closePort()
    myArd.closePort()
    print(dictVars)
    
if __name__ == "__main__" :
    run()


