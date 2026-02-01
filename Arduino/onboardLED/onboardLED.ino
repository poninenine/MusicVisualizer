
// This code needs to read serial data and respond with lights accordingly

// For now, we will just blink the onboard LED before extending functionality

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  delay(1500);
}

void blink() {
  // Response upon receiving serial indicator
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(50);                      // wait
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
  // delay(100); 
}

void blinkTwice() {
  // Response upon receiving serial indicator
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(50);                      // wait
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
  delay(50);  
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(50);                      // wait
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW

}

// the loop function runs over and over again forever
void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    int incomingByte = 0;
    // read the incoming byte:
    incomingByte = Serial.read();

    if (incomingByte == 'k') {
      blink();
    } else if (incomingByte == 's') {
      blinkTwice();
    }

    // say what you got:
    // Serial.print("I received: ");
    // Serial.println(incomingByte, DEC);
  }
}