

// SimpleTx - the master or the transmitter

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include<Wire.h>
#include <stdlib.h>

#define CE_PIN  9
#define CSN_PIN 10

const byte slaveAddress[6] = "11001" ;


RF24 radio(CE_PIN, CSN_PIN); // Create a Radio


const String tempIdent = "T";
const String accxIdent = "X";
const String accyIdent = "Y";
const String acczIdent = "Z";
const String gyrxIdent = "x";
const String gyryIdent = "y";
const String gyrzIdent = "z";
const String soundIdent = "s";
const String lastChar = "end";
String numbers;
String stringToSend1;
String stringToSend2;
char message1[32];
char message2[32];


char txNum = '0';


unsigned long currentMillis;
unsigned long prevMillis;
unsigned long txIntervalMillis = 1000; // send once per second

const int MPU=0x68; 
int AcX,AcY,AcZ,GyX,GyY,GyZ;
int Tmp;
String AccX, AccY, AccZ, Temp, GyrX, GyrY, GyrZ, Sound;
int Snd;

void setup() {
    
    Serial.begin(9600);

    Serial.println("SimpleTx Starting");

    radio.begin();
//    radio.setDataRate( RF24_250KBPS );
    radio.setPALevel(RF24_PA_MIN);
//    radio.setRetries(3,5); // delay, count
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
    Snd = analogRead(A0);
   
    /*
    currentMillis = millis();
    if (currentMillis - prevMillis >= txIntervalMillis) {
        send();
        prevMillis = millis();
    }
    */

    Tmp = Tmp/340 + 36.25;
    sendAll();
/*
    dataToSend = AcY;
    send();
    dataToSend = AcZ;
    send();
    dataToSend = Sound;
    send();
    delay(10);
    */
    /*
    Serial.print("GyY: ");
    Serial.print(GyY);
    Serial.println(); 
    */
    
}

//====================
/*
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

*/


void sendAll() {

    bool rslt;
    AccX = String(AcX);
    AccY = String(AcY);
    AccZ = String(AcZ);
    GyrX = String(GyX);
    GyrY = String(GyY);
    GyrZ = String(GyZ);
    Temp = String(Tmp);
    Sound = String(Snd);
    stringToSend1 = tempIdent + Temp + accxIdent + AccX + accyIdent + AccY + acczIdent + AccZ + lastChar; 
    stringToSend2 = gyrxIdent + GyrX + gyryIdent + GyrY + gyrzIdent + GyrZ + soundIdent + Sound + lastChar;

    stringToSend1.toCharArray(message1, stringToSend1.length());
    stringToSend2.toCharArray(message2, stringToSend2.length());

    radio.write( &message1, sizeof(message1) );
    radio.write( &message2, sizeof(message2));
        
//    Serial.print("Data Sent ");
    Serial.println(message1);
    Serial.println(message2);
    
}


