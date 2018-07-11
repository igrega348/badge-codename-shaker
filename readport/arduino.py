import serial
from datetime import datetime

class Arduino():
    def __init__(self, filename):
        self.ser = serial.Serial('com6', 9600)
        self.ser.flushInput()
#        self.connect_arduino()
        self.filename = filename

    def connect_arduino(self):
        print("Trying to connect")
        file = open(self.filename,mode='wb')
        a = datetime.now()
        b = datetime.now()
        dt = b-a
        while dt.seconds <= 10:
#            if self.ser.inWaiting() > 0:
#                data = self.ser.read()
#                file.write(data)
#
            data = self.ser.read()
            file.write(data)
            b = datetime.now()
            dt = b-a
        file.close()
        self.ser.close()