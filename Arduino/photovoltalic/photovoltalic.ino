/*
  ReadAnalogVoltage

  Reads an analog input on pin 0, converts it to voltage, and prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/ReadAnalogVoltage
*/

int fadeAmount = 1;
int brightness = 0;
int led = 9;
int dig2 = 0;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // setup pin 9 to led
  pinMode(led, OUTPUT);
  // setup onboard led
  pinMode(LED_BUILTIN, OUTPUT);
  //set up digital input at pin 2
  pinMode(2, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue;
  // print out the value you read:
  Serial.println(voltage);
  
  //read input 2
  dig2 = digitalRead(2);
  //print status
  
  //if digital input high, then light up LED
  if (dig2 == HIGH) {
    digitalWrite(LED_BUILTIN, HIGH);
  } else if(voltage <= 120) {
    digitalWrite(LED_BUILTIN, LOW);
  }
  else{
    digitalWrite(LED_BUILTIN, HIGH);
  }
  
  // set the brightness of pin 9
  analogWrite(led, brightness);
  //increment brightness
  brightness += fadeAmount;
  // not ignore overflow
  if (brightness <= 0 || brightness >= 255) {
    fadeAmount = -fadeAmount;
  }
  //wait
  delay(10);
}
