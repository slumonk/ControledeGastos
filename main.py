# -*- coding: utf-8 -*-

import time

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.properties import StringProperty

class Manager(ScreenManager):
    pass

class Rodape(BoxLayout):
	hora = StringProperty()
	def __init__(self, **kwargs):
		super(Rodape, self).__init__(**kwargs)
		self.hora = time.asctime()[11:19]
		Clock.schedule_interval(self.updateHora, 1)

	def updateHora(self, *args):
		
		self.ids.horario.text = str(self.hora)

class Home(Screen):
	def __init__(self, **kwargs):
		super(Home, self).__init__(**kwargs)
		#Clock.schendule_interval(Rodape().updateHora(), 1)

class Objetivos(Screen):
	pass

class Historico(Screen):
	pass

class ControleApp(App):
    def build(self):
       return Manager()

if __name__ == '__main__':
    ControleApp().run()
