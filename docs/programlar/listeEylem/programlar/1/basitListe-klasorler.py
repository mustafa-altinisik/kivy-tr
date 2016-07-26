# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.uix.listview import ListView

import os

class basitListeUyg(App):

    def build(self):
        duzen=BoxLayout()
	
        dizin_icerik=os.listdir("/usr")
	
        basit_liste_adaptoru = SimpleListAdapter(data=dizin_icerik, cls=Button)

        liste = ListView(adapter=basit_liste_adaptoru)
        
        duzen.add_widget(Label(text="/usr dizini"))
        duzen.add_widget(liste)

        return duzen
      
basitListeUyg().run()
