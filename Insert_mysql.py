
import mysql.connector

cnx = mysql.connector.connect(user='adrian', password='1234',
                                 host='127.0.0.1',
                                 database='RFID')
cursor = cnx.cursor()
query = ("INSERT INTO rfid (nombre,texto,rfid) VALUES ('Hugo Vargas','Test Python 1',88843565);")


cursor.execute(query)
cnx.commit()

cursor.close()
cnx.close()

