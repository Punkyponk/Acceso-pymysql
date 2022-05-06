from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from GridLayoutColor import GridLayoutColor
#####
import json
import pymysql.cursors

        
class kivydb(App):
    def btn_press(self, obj):
        if self.connection:
            print(self.txi_nick.text, self.txi_passwd.text)
            nick = self.txi_nick.text
            passwd = self.txi_passwd.text
            ##########################################
            #Defino el cursor, pero aun no tiene ningun trabajo
            MiCursor = self.connection.cursor()
            #SQL a ejecutar
            SQL = 'SELECT * FROM usuario WHERE nick=%s AND password=sha2(%s,256)'
            MiCursor.execute(SQL,[nick,passwd])
            Resultado = MiCursor.fetchone()
            if Resultado:
                print("Acceso Concedido")
                self.lbl_blank2.text="Acceso Concedido"
            else:
                print("Acceso Denegado")
                self.lbl_blank2.text="Acceso Denegado"
        else:
            print("Error")
            self.lbl_blank2.text="Error"
    
    def iniciarDB(self):
        self.Conf = None
        with open("db.json") as jsonfile:
            self.Conf = json.load(jsonfile)
        self.connection = pymysql.connect(
            host=self.Conf['HOST'], user=self.Conf['DBUSER'],
            password=self.Conf['DBPASS'], database=self.Conf['DBNAME'],
            charset='utf8mb4', port=self.Conf['PORT']
        )
        
    def __init__(self,**kwargs):
        #Llamar al constructor de la clase base (App)
        super().__init__(**kwargs)    
	
    def build(self):
        self.gdl_principal = GridLayoutColor(cols=3,rows=1)
        self.gdl_principal._update_color([0,0,1,1])
        #1.Etiqueta
        self.lbl_blank = Label(text="")
        self.gdl_principal.add_widget(self.lbl_blank)
        #2.Grid medio
        self.gdl_medio = GridLayoutColor(rows=5)
			#Widgets
        self.lbl_nick = Label(text="usuario")
        self.txi_nick = TextInput(text="", multiline=False)
        self.lbl_passwd = Label(text="contraseña")
        self.txi_passwd = TextInput(text="", password=True, multiline=False)
        self.btn = Button(text="accesar")
			#Modificaciones
        self.gdl_medio._update_color([1,0,0,1])
        self.btn.bind(on_press=self.btn_press)
			#Agregar
        self.gdl_medio.add_widget(self.lbl_nick)
        self.gdl_medio.add_widget(self.txi_nick)
        self.gdl_medio.add_widget(self.lbl_passwd)
        self.gdl_medio.add_widget(self.txi_passwd)
        self.gdl_medio.add_widget(self.btn)
        self.gdl_principal.add_widget(self.gdl_medio)
		#3.Etiqueta
        self.lbl_blank2 = Label(text="")
        self.gdl_principal.add_widget(self.lbl_blank2)
        return self.gdl_principal

if __name__ == '__main__':
    #Acceso().iniciarDB()
    kdb = kivydb()
    kdb.iniciarDB()
    #Ejecutar el entorno gráfico
    kdb.run()
