from arduinoStream import Arduino
from datetime import datetime
from analyseStream import loop, initialiseDict
from readPortStream import screen
from curveFit import fitHarmonic
import numpy as np



def initialise():
    
    myArd = Arduino()
    return myArd


def getLimits(arduino, dictLimits):
    #get a 10 second screening from the sensors as a dictionary of variables
    print('Started screening')
    samples = screen(arduino)
    print('Done screening')
#    print(samples)
    
    for variable in samples:
        #when the dictionary is 'End' then it is empty and exceptions are raised
        if len(samples[variable]) == 0:
#            print('Empty')
            pass
        else:
            low, high = fitHarmonic(samples[variable])
           
            dictLimits[variable] = (low, high)
    
    try:
        dictLimits['Tmp'] = (10,30)
    except:
        pass
        
    return dictLimits
    
         
    
def run():
    myArd = initialise()
    dictIdent, dictVars = initialiseDict()
    dictLimits = dict()
#    a = datetime.now()
#    b = datetime.now()
#    dt = b - a
    dictLimits = getLimits(myArd, dictLimits)
    print('Got limits')
    dictMessages = {'Snd':'Too loud',
                  'AcZ':'Shake',
                  'AcX':'Shake',
                  'AcY':'Shake',
                  'GyX':'Rotate',
                  'GyY':'Rotate',
                  'GyZ':'Rotate',
                  'Tmp':'Hot'}
    
    try:
        while True:    
            try:
#                print(len(dictVars['Snd']))
    #            b = datetime.now()
    #            dt = b-a
                data = myArd.readData()
                data = str(data, 'utf-8')
                if data == None:
                    pass
                else:
                    newDict = loop(data, dictIdent)
                #if the recorded value is bigger than the limit, print the message    
                for key in newDict:
                    if key in dictLimits:
                        if newDict[key] < dictLimits[key][0] or newDict[key] > dictLimits[key][1]:
                            print(newDict[key])
                            print(dictMessages[key])
    #            print(data)
            except KeyboardInterrupt:
                print('Keyboard interrupt detected')
                myArd.closePort()
    #            print(dictVars)
                break
#            except:
#                myArd.closePort()
    except KeyboardInterrupt:
        print('Keyboard Interrupt Detected')
        myArd.closePort()
        pass

    myArd.closePort()
    
if __name__ == "__main__" :
    run()
#    getLimits()


