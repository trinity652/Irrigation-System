import serial
import csv
ser = serial.Serial('/dev/ttyACM1', 9600)
x=[]
i=0
with open('soilmoisture.txt','wb') as text_file:
 writer=csv.writer(text_file)
 while i<=100:
  data=str(ser.readline().rstrip())
  x.append(data)
  print(data)
  writer.writerows(x[i])
  i=i+1
 
	
