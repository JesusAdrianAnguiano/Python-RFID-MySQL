# Bibliotecas
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import mysql.connector

print("Conectando")
cnx = mysql.connector.connect(user='adrianlan', password='1234',
                                 host='192.168.100.157',
                                 database='RFID')
cursor = cnx.cursor()
print("Conectado a la base de datos")

# Inicar el sensor
reader = SimpleMFRC522()

# Cuerpo del programa
try:
    # Leer el tag
    while True:
        print("Acercar el tag al lector")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise

query = ("INSERT INTO rfid (texto,rfid) VALUES ("%s %s % (id,text)";")


cursor.execute(query)
cnx.commit()

cursor.close()
cnx.close()



