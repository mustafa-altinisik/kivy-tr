# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from kivy.uix.actionbar import ActionBar
from kivy.uix.actionbar import ActionView
from kivy.uix.actionbar import ActionButton
from kivy.uix.actionbar import  ActionPrevious

class eylemCubugu(App):

    def dugmeyeTikla(self, nesne):
        self.etiket.text="Eylem düğmesine tıklandı"

    def build(self):
    
        eylemcubugu= ActionBar(pos_hint= {'top':1})

        eylemgorunumu=ActionView()
        eylemcubugu.add_widget(eylemgorunumu)

        oncekieylem=ActionPrevious(title='Eylem Çubuğu')
        eylemgorunumu.add_widget(oncekieylem)
        
        eylemdugmesi=ActionButton(text="Eylem Düğmesi")
        eylemgorunumu.add_widget(eylemdugmesi)
        eylemdugmesi.bind(on_press=self.dugmeyeTikla)
        
        duzen = BoxLayout(orientation='vertical')
        duzen.add_widget(eylemcubugu)

        self.etiket=Label(text="Ana Alan")
        duzen.add_widget(self.etiket)
        
        return duzen

eylemCubugu().run()
