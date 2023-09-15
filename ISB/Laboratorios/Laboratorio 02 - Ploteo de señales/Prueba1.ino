unsigned long lastMsg = 0;
float F=1;                   //1hz
double Fs = 10*F;            //10 hz
double Ts_ms = (1/Fs)*1000;  //100 ms
int input;

void setup(){
  Serial.begin(9600);
  while(!Serial);
  
}
void loop() {
  unsigned long now = millis();
  
  if (now - lastMsg > Ts_ms){
    
    lastMsg = now;

    int r1 = analogRead(A2);
    Serial.println(r1);
  }
}
