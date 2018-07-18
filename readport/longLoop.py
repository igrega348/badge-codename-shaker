from arduinoStream import Arduino
from datetime import datetime
import time
from analyseStream import loop, initialiseDict
from readPortStream import screen
from curveFit import fitHarmonic, getImage
import numpy as np
from message_parent import EchoBot
from apscheduler.schedulers.background import BackgroundScheduler
import copy


def initialise():
    
    myArd = Arduino()
    return myArd


def getLimits(arduino, dictLimits):
    emptyDict = dict()
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
        dictLimits['Tmp'] = (10,40)
    except:
        pass
    
#    dictLimits = copy.deepcopy(emptyDict)
#    print(dictLimits)
        

def plotData(dictVars):
    for key in dictVars:
        if len(dictVars[key]) == 0:
            pass
        else:
            getImage(dictVars[key], key)
    
         
    
def run():
    client = EchoBot("<username>", "<password>")
    
    myArd = initialise()
    dictIdent, dictVars = initialiseDict()
    dictLimits = dict()
#    a = datetime.now()
#    b = datetime.now()
#    dt = b - a
    
    getLimits(myArd, dictLimits)
    
#    print(dictLimits)
    #run this in background at every time interval
    limits = BackgroundScheduler()
    limits.start()
    limits.add_job(func = plotData, trigger = 'interval',
                   seconds = 30,
                   args = [dictVars])
#    limits.add_job(func = getLimits, trigger = 'interval',
#                   minutes = 2, 
#                   args = [myArd, dictLimits])
#    
    
    

    print('Got limits')
    dictMessages = {'Snd':'Too loud',
                  'AcZ':'Shake',
                  'AcX':'Shake',
                  'AcY':'Shake',
                  'GyX':'Rotate',
                  'GyY':'Rotate',
                  'GyZ':'Rotate',
                  'Tmp':'Hot'}
    
    times = []
    times.append(datetime.now())
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
                    newDict = loop(data, dictIdent, dictVars)
#                detected = False
                #if the recorded value is bigger than the limit, print the message    
                for key in newDict:
                    if key in dictLimits:
                        if (newDict[key] < dictLimits[key][0] or newDict[key] > dictLimits[key][1]) and (datetime.now()-times[-1]).seconds > 2:
                            client.message_somebody(dictMessages[key],
                                                    thread_id=client.THREAD_ID_ECHOBOT_TO_IVAN)
                            print(newDict[key])
                            print(dictMessages[key])
#                            detected = True
                            times.append(datetime.now())
#                            newDict = {}
#                            break
#                if detected == True:
#                    time.sleep(2)
#                    detected = False
    #            print(data)
            except KeyboardInterrupt:
                print('Keyboard interrupt detected')
                myArd.closePort()
                limits.shutdown()
    #            print(dictVars)
                break
#            except TypeError:
#                pass
            except:
                myArd.closePort()
                limits.shutdown()
    except KeyboardInterrupt:
        print('Keyboard Interrupt Detected')
        myArd.closePort()
        limits.shutdown()
        
    finally:
        myArd.closePort()
    
#    limits.shutdown()
    myArd.closePort()
    
if __name__ == "__main__" :
    run()
#    getLimits()


