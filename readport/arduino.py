import serial

class Arduino():
    def __init__(self, filename):
        self.ser = serial.Serial('com6', 9600)
        self.ser.flushInput()
#        self.connect_arduino()
        self.filename = filename

    def connect_arduino(self):
        print("Trying to connect")
        file = open(self.filename,mode='wb')
        i = 0
        while i<=10000:
            if self.ser.inWaiting() > 0:
                data = self.ser.read()
                file.write(data)
                i += 1
        file.close()
        self.ser.close()