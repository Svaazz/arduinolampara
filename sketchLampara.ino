int rele = 9;
int msg;

void setup()
{
   pinMode(rele, OUTPUT);
   Serial.begin(9600); //iniciando Serial
}
 
void loop()
{
   if (Serial.available() > 0)
   {
      msg = Serial.read(); //leo el serial
 
      if(msg == 'v')
      {
         digitalWrite(rele, HIGH); //si entra una 'v' se enciende la luz
      }
      else if(msg == 'b')
      {
         digitalWrite(rele, LOW); //si entra una 'b' se apaga
      }
   }
}
