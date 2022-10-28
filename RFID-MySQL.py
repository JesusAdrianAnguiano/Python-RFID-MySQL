
# Bibliotecas
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import mysql.connector

cnx = mysql.connector.connect(user='adrianln', password='1234',
                                 host='192.168.100.157',
                                 database='RFID')


# Inicar el sensor
reader = SimpleMFRC522()

# Cuerpo del programa
try:
    # Leer el tag
    while True:
        print("Acercar el tag al lector")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        cursor = cnx.cursor()
        query = ("INSERT INTO rfid (texto,rfid) VALUES ('"+ text +"','"+ id +"');")
        cursor.execute(query)
        cnx.commit()
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
    cursor.close()
    cnx.close()

