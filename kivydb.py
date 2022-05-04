from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty
from kivy.graphics import Color, Rectangle

class GridLayoutColor(GridLayout):
    def __init__(self,**kwargs):
        super(GridLayoutColor, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0,0,1,1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        
class kivydb(App):
	#Este es el constructor
    def __init__(self,**kwargs):
        #Llamar al constructor de la clase base (App)
        super().__init__(**kwargs)    
	#Todos los elementos visuales se definene o encadenan aqui
    def build(self):
		#Vamos a definir un layout
        gdl_principal = GridLayout(cols=3,rows=1)
        #1.Etiqueta
        lblvacio = Label(text=" ")
        lblvacio.background_color = ListProperty([0.19,0.94,0.06,1])
        gdl_principal.add_widget(lblvacio)
        #2.Grid medio
        gdl_medio = GridLayoutColor(rows=5)
			#Widgets
        lbl_nick = Label(text="usuario")
        txi_nick = TextInput(text="")
        lbl_passwd = Label(text="contraseña")
        txi_passwd = TextInput(text="")
        btn = Button(text="")
			#Modificaciones
        txi_passwd.password = True
			#Agregar
        gdl_medio.add_widget(lbl_nick)
        gdl_medio.add_widget(txi_nick)
        gdl_medio.add_widget(lbl_passwd)
        gdl_medio.add_widget(txi_passwd)
        gdl_medio.add_widget(btn)
        gdl_principal.add_widget(gdl_medio)
		#3.Etiqueta
        lblvacio2 = Label(text=" ")
        lblvacio2.background_color = ListProperty([1,1,1,1])
        gdl_principal.add_widget(lblvacio2)
        #######
        self.gdl_principal = gdl_principal
        return gdl_principal

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    kdb = kivydb()
    kdb.run()
