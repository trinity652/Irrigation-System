`int volta[2];
int Pin1=12;
int Pin2=11;
int Pin3=7;
float volta_val[2];
float mean_val[2];
float old_volta_val[2];
int i,j=0,k=0,l=0;
void setup()
{
  volta[0]=A0;
  volta[1]=A1;
  pinMode(Pin1,OUTPUT);
  pinMode(Pin2,OUTPUT);
  pinMode(Pin3,OUTPUT);
  Serial.begin(9600);
  for(i=0;i<2;i++)
  {
    volta_val[i]=0;
    mean_val[i]=0;
    old_volta_val[i]=0;
  }
  i=0;
}
void loop()
{
   for(i=0;i<2;i++)
  {
   volta_val[i]=analogRead(volta[i]);//The analog input is read 
   volta_val[i]=(volta_val[i]/1024)*5;//The value is converted into coresponding volts
  }
  Serial.println(volta_val[0]);
  Serial.println(volta_val[1]);
  for(i=0;i<2;i++)
  {
   if(j<100)
   {
     mean_val[i]=mean_val[i]+volta_val[i];
   }
  }
  if(j==100)
  {
      for(i=0;i<4;i++)
      {
          old_volta_val[i]=mean_val[i]/100;
      }
  }
j++;
if(old_volta_val[0]>1.50 || old_volta_val[1]>1.50)
digitalWrite(Pin3,HIGH);
else
digitalWrite(Pin3,LOW);
if(old_volta_val[0]>1.50)
digitalWrite(Pin1,LOW);
else
digitalWrite(Pin1,HIGH);
if(old_volta_val[1]>1.50)
digitalWrite(Pin2,LOW);
else
digitalWrite(Pin2,HIGH);

if(j>100)
{
    for(i=0;i<4;i++)
    {
        mean_val[i]=0;
    }
    j=0;
}
}
  
