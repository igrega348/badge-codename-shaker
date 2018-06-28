int set = 0;
int reset = 0;

void setup() {
  pinMode(9, OUTPUT);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  set = digitalRead(2);
  reset = digitalRead(3);

  if (set == HIGH){
    digitalWrite(9, HIGH);
  } else if (reset == HIGH) {
    digitalWrite(9, LOW);
  }

}
