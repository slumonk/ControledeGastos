# -*- coding: utf-8 -*-

import time
from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.properties import StringProperty


class Manager(ScreenManager):
    pass

class Rodape(BoxLayout):
	data_hora_atual = datetime.now()
	data_atual = data_hora_atual.strftime('%d/%m/%Y')
	def __init__(self, **kwargs):
		super(Rodape, self).__init__(**kwargs)
		
		Clock.schedule_interval(self.updateHora, 1)

	def updateHora(self, *args):
		self.ids.datahoje.text = self.data_atual
		self.ids.horario.text = time.asctime()[11:19]

class Home(Screen):
	def __init__(self, **kwargs):
		super(Home, self).__init__(**kwargs)

	def alteraEntrada(self, *args):
		self.verificador = 'entrada'
		self.popAltera()

	def alteraGastos(self, *args):
		self.verificador = 'gastos'
		self.popAltera()

	def popAltera(self):
		boxPop = BoxLayout(orientation='vertical')
		self.pop = Popup(title='Alterar valores', content=boxPop,
		size_hint=(None,None), size=(400, 500))
		self.pop.open()

class Objetivos(Screen):
	pass

class Historico(Screen):
	pass

class ControleApp(App):
    def build(self):
       return Manager()

if __name__ == '__main__':
    ControleApp().run()
