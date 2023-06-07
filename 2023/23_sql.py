#  Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente
#  base de datos MySQL:
#  - Host: mysql-5707.dinaserver.com
#  - Port: 3306
#  - User: mouredev_read
#  - Password: mouredev_pass
#  - Database: moure_test

#  Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
#  - SELECT * FROM `challenges`

#  Se pueden usar librerías para realizar la lógica de conexión a la base de datos.

import pymysql

host = 'mysql-5707.dinaserver.com'
# Port: 3306
usuario = 'mouredev_read'
password =  'mouredev_pass'
db=  'moure_test'


conexion = pymysql.connect(
host=host,
user=usuario,
password=password,
db=db,
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)

cursor = conexion.cursor()

sql = "SELECT * FROM challenges"

cursor.execute(sql)
datos = cursor.fetchall()

cursor.close()
conexion.close()

for dato in datos:
    print (dato)

