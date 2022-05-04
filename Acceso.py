##TAREA: COMO USAR SHA2 EN PYTHON Y COMO FUNCIONA DATETIME

import json
import pymysql.cursors
Conf = None
with open("db.json") as jsonfile:
	Conf = json.load(jsonfile)
	
#sudo apt-get install python3-mysqldb (Instalar en Ubuntu)

connection = pymysql.connect(
    host=Conf['HOST'],user=Conf['DBUSER'],
    password=Conf['DBPASS'],database=Conf['DBNAME'],
    charset='utf8mb4',port=Conf['PORT']
)

if connection :
	print("Se pudo establecer la conexion")
	#############################################
	#Defino el cursor, pero aun no tiene ningun trabajo
	MiCursor = connection.cursor()
	#SQL a ejecutar
	SQL = "Select * from usuario"
	Micursor.execute(SQL)
	#############################################
	#Fetchall
	Resultado = MiCursor.fetchall()
	for fila in Resultado:
		print(type(fila))
		print(fila)
		print("Id",fila[0])
		print("Tipo",fila[1])
		print("Nick",fila[2])
	
else:
	print("No se pudo establecer la conexion")

#Cerrar la conexion
connection.close()
