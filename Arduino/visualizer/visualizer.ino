
// This code needs to read serial data and respond with lights accordingly

// There are three kinds of lights in this version, one each for click, kick, and snare
int whitePin = 11;  // Click light
int redPin = 10;  // Kick light
int yellowPin = 9;  // Snare light

// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(9600);
  delay(1500);
  digitalWrite(LED_BUILTIN, LOW);
}

void blink(int pin) {
  // Response upon receiving serial indicator
  analogWrite(pin, 255);  // turn the LED on (HIGH is the voltage level)
  delay(50);                      // wait
  analogWrite(pin, 0);   // turn the LED off by making the voltage LOW
  // delay(100); 
}

// the loop function runs over and over again forever
void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    int incomingByte = 0;
    // read the incoming byte:
    incomingByte = Serial.read();

    switch (incomingByte) {
      case 'c':
        blink(whitePin);
        break;

      case 'k':
        blink(redPin);
        break;

      case 's':
        blink(yellowPin);
        break;
    }

  }
}