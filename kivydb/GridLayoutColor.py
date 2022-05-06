from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.graphics import Color, Rectangle


class GridLayoutColor(GridLayout):
    background_color = ListProperty([1,0,0,1])
    
    def __init__(self,**kwargs):
        super(GridLayoutColor, self).__init__(**kwargs)
        self._update_color(self.background_color)
        self.bind(pos=self._update_rect)
        self.bind(size=self._update_rect)
        
    def _update_color(self, BC):
        self.canvas.before.clear()
        with self.canvas.before:
            R,G,B,A = self.background_color = BC
            Color(R,G,B,A)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            
    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
