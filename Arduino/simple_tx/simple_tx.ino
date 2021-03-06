

// SimpleTx - the master or the transmitter

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include<Wire.h>

#define CE_PIN  9
#define CSN_PIN 10

const byte slaveAddress[6] = "00001" ;


RF24 radio(CE_PIN, CSN_PIN); // Create a Radio

float dataToSend = 123.456;
float TempIdentifier = 0.0;
float AcXIdentifier = 1.0;
float AcYIdentifier = 2.0;
float AxZIdentifier = 3.0;

char txNum = '0';


unsigned long currentMillis;
unsigned long prevMillis;
unsigned long txIntervalMillis = 1000; // send once per second

const int MPU=0x68; 
float AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;
float Sound;

void setup() {
    
    Serial.begin(9600);

    Serial.println("SimpleTx Starting");

    radio.begin();
    radio.setDataRate( RF24_250KBPS );
    radio.setRetries(3,5); // delay, count
    radio.openWritingPipe(slaveAddress);
    Wire.begin();
    Wire.beginTransmission(MPU);
    Wire.write(0x6B); 
    Wire.write(0);    
    Wire.endTransmission(true);
}

//====================

void loop() {
    Wire.beginTransmission(MPU);
    Wire.write(0x3B);  
    Wire.endTransmission(false);
    Wire.requestFrom(MPU,12,true);  
    AcX=Wire.read()<<8|Wire.read();    
    AcY=Wire.read()<<8|Wire.read();  
    AcZ=Wire.read()<<8|Wire.read();  
    Tmp=Wire.read()<<8|Wire.read();
    GyX=Wire.read()<<8|Wire.read();  
    GyY=Wire.read()<<8|Wire.read();  
    GyZ=Wire.read()<<8|Wire.read();  
    Sound = analogRead(A0);
    Serial.println("trying");
    /*
    currentMillis = millis();
    if (currentMillis - prevMillis >= txIntervalMillis) {
        send();
        prevMillis = millis();
    }
    */

    dataToSend = Tmp/340 + 36.25;
    send();
    dataToSend = AcX;
    send();
    dataToSend = AcY;
    send();
    dataToSend = AcZ;
    send();
    dataToSend = Sound;
    send();
    delay(10);
    /*
    Serial.print("Tmp: ");
    Serial.print(Tmp);
    Serial.println(); 
    */
}

//====================

void send() {

    bool rslt;
    rslt = radio.write( &dataToSend, sizeof(dataToSend) );
        // Always use sizeof() as it gives the size as the number of bytes.
        // For example if dataToSend was an int sizeof() would correctly return 2

    Serial.print("Data Sent ");
    Serial.print(dataToSend);
    if (rslt) {
        Serial.println("  Acknowledge received");
      //  updateMessage();
    }
    else {
        Serial.println("  Tx failed");
    }
}

void sendTemp() {

    bool rslt;
    rslt = radio.write( &dataToSend, sizeof(dataToSend) );
        // Always use sizeof() as it gives the size as the number of bytes.
        // For example if dataToSend was an int sizeof() would correctly return 2

    Serial.print("Data Sent ");
    Serial.print(dataToSend);
    if (rslt) {
        Serial.println("  Acknowledge received");
      //  updateMessage();
    }
    else {
        Serial.println("  Tx failed");
    }
}

void sendAccel() {

    bool rslt;
    rslt = radio.write( &dataToSend, sizeof(dataToSend) );
        // Always use sizeof() as it gives the size as the number of bytes.
        // For example if dataToSend was an int sizeof() would correctly return 2

    Serial.print("Data Sent ");
    Serial.print(dataToSend);
    if (rslt) {
        Serial.println("  Acknowledge received");
      //  updateMessage();
    }
    else {
        Serial.println("  Tx failed");
    }
}

void sendGyro() {

    bool rslt;
    rslt = radio.write( &dataToSend, sizeof(dataToSend) );
        // Always use sizeof() as it gives the size as the number of bytes.
        // For example if dataToSend was an int sizeof() would correctly return 2

    Serial.print("Data Sent ");
    Serial.print(dataToSend);
    if (rslt) {
        Serial.println("  Acknowledge received");
      //  updateMessage();
    }
    else {
        Serial.println("  Tx failed");
    }
}

//================
/*
void updateMessage() {
        // so you can see that new data is being sent
    txNum += 1;
    if (txNum > '9') {
        txNum = '0';
    }
    dataToSend[8] = txNum;
}

*/

