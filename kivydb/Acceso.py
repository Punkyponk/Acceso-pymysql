#sudo apt-get install python3-mysqldb
#python3 -m pip install PyMySQL

import json
import pymysql.cursors
from getpass import getpass

Conf = None
with open("db.json") as jsonfile:
	Conf = json.load(jsonfile)
	
"""connection = pymysql.connect(host='localhost', user='user',
	password='passwd', database='db', charset='utf8mb4', port=3306)"""

connection = pymysql.connect(host=Conf['HOST'], user=Conf['DBUSER'],
	password=Conf['DBPASS'], database=Conf['DBNAME'], charset='utf8mb4',
	port=Conf['PORT'])

if connection:
	print("Se pudo establecer la conexion")
	nick = input("Dame tu nombre de acceso: ")
	passwd = getpass("Dame tu contraseña: ")
	##########################################
	#Defino el cursor, pero aun no tiene ningun trabajo
	MiCursor = connection.cursor()
	#SQL a ejecutar
	SQL = 'SELECT * FROM usuario WHERE nick=%s AND password=sha2(%s,256)'
	MiCursor.execute(SQL,[nick,passwd])
	Resultado = MiCursor.fetchone()
	if Resultado:
		print("Acceso Concedido")
	else:
		print("Acceso Denegado")
	"""
	##########################################
	#FetchAll
	
	for fila in Resultado:
		print(type(fila))
		print("Id", fila[0])
		print("Tipo", fila[1])
		print("Nick", fila[2])
	"""
else:
	print("No se pudo establecer la conexion")

#Cerra la conexion
connection.close()
