# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.uix.listview import ListView

class basitListeUyg(App):

    def build(self):
        duzen=BoxLayout()
	
        programlama_dilleri=["Perl", "PHP", "Pure", "Python", "Rebol",
                             "Rexx", "Ruby", "Scheme", "Tcl"]
	
        basit_liste_adaptoru = SimpleListAdapter(data=programlama_dilleri, cls=Button)

        liste = ListView(adapter=basit_liste_adaptoru)
        
        duzen.add_widget(Label(text="Programlama Dilleri"))
        duzen.add_widget(liste)

        return duzen
      
basitListeUyg().run()
