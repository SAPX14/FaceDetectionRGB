#include<cvzone.h>
SerialData serialData;
int sendVals[2];
void setup() {
  // put your setup code here, to run once:
  serialData.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int potVal = analogRead(A0);
  sendVals[0] = potVal;
  serialData.Send(sendVals);
}
