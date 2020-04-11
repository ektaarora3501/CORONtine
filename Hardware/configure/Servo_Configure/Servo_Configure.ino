// To test different positions of Servo Arm at different angles
#include <Servo.h>  
int servoPin = 3;  
int vcc = 7;

Servo Servo1; 
void setup() { 
   Servo1.attach(servoPin);
   pinMode(vcc, OUTPUT);
   digitalWrite(vcc, HIGH);
}

void loop(){ 
   // Make servo go to 0 degrees 
   Servo1.write(0); 
   delay(1000); 
}
