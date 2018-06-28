import serial
import time

class Arduino():

    def connect_arduino(self):
        conn = False
        print("Searching for Arduino...")
        while not conn:
            if(self.ser.inWaiting()>0):
                data = self.ser.read()
                data = str(data)
                print(data)
#                if data == 'a':
#                    self.ser.write('a')
#                    time.sleep(0.001)
#                if data == 'b':
#                    self.ser.flush()
#                    self.ser.write('b')
#                    conn = True
#                    print "Connection to Arduino established"
#                time.sleep(0.001)

    def __init__(self):
        self.ser = serial.Serial('COM6', 9600)
        self.ser.flushInput()
        self.connect_arduino()

    def send_command(self, command):
        self.ser.write(command)
    
        
