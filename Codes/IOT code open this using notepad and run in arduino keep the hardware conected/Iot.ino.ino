String readString;
void setup() {
  // put your setup code here, to run once:
pinMode(2,OUTPUT);
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
while(!Serial.available()) {}
  // serial read section
  while (Serial.available())
  {
    //if (Serial.available() >0)
    //{
      String c = Serial.readString();  //gets one byte from serial buffer
      readString = c; //makes the string readString
    //}
  }

  if (readString.length() >0)
  {
    Serial.print("Arduino received: ");  
    Serial.println(readString); //see what was received
    if(readString=="found")
    {
      digitalWrite(2,HIGH);
      
    }
    else
    {
      digitalWrite(2,LOW);
    }
  }

  delay(500);

}
