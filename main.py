# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class Manager(ScreenManager):
    pass

class Home(Screen):
    pass
class Menu(BoxLayout):
    pass

class MyApp(App):
    def build(self):
       return Manager()

if __name__ == '__main__':
    MyApp().run()