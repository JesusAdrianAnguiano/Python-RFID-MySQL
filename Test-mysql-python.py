
from mysql.connector import (connection)
print(conectandose a la base de datos)
cnx = connection.MySQLConnection(user='adrian', password='1234',
                                 host='127.0.0.1',
                                 database='coviddetector')
print(conexión realizada)
print(cnx)

print(cerrar conexión)
cnx.close()
print(conexión cerrada)

