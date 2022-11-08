
import mysql.connector

cnx = mysql.connector.connect(user='adrianlan', password='1234',
                                 #user='adrian', password='1234', correr en máquina virtual
                                 #host='127.0.0.1', correr en máquina virtual
                                 host='192.168.100.157',
                                 database='coviddetector')
cursor = cnx.cursor()
query = ("SELECT id, nombre, temp FROM registro WHERE temp>40")


cursor.execute(query)

for (id, nombre, temp) in cursor:
  print(id, nombre, temp)

cursor.close()
cnx.close()