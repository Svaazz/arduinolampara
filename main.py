import serial
import os
pu = '/dev/ttyACM0' #El puerto suele cambiar cada vez que conectas el serial, asi que hay que cambiarlo tambien aqui
ser = serial.Serial(pu, 9600) #inicializo el puerto de serie a 9600 baud
print("Introduce un comando ('s' para salir | 'v' para apagar | 'b' para encender): ")
entrada = raw_input()
 
while entrada != 's':
   os.system('clear')
   ser.write(entrada) #envia la entrada por serial
   print("Introduce un comando ('s' para salir): ")
 
   entrada = raw_input()
