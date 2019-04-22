# -*- coding: utf-8 -*-

import time
from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.properties import StringProperty

class Manager(ScreenManager):
    pass

class Rodape(BoxLayout):
	data_hora_atual = datetime.now()
	data_atual = data_hora_atual.strftime('%d/%m/%Y')
	#hora_atual = 	
	def __init__(self, **kwargs):
		super(Rodape, self).__init__(**kwargs)
			
		
		Clock.schedule_interval(self.updateHora, 1)

	def updateHora(self, *args):
		self.ids.datahoje.text = self.data_atual
		self.ids.horario.text = time.asctime()[11:19]

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
