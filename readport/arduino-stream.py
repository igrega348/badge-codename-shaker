import serial

class Arduino():
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.ser.flushInput()
#        self.connect_arduino()
       

    def readData(self):
#        print("Trying to connect")
        if self.ser.inWaiting() > 0:
            data = self.ser.read()
        return data   
    
    def closePort(self):
        self.ser.close()