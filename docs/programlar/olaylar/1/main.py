# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class olayUyg(App):

    def metni_degistir(self, nesne):
        self.dugme.text='Tıkladın ve değiştim.'

    def build(self):
        duzen=BoxLayout()
        self.dugme=Button(text='Değiştir')
        self.dugme.bind(on_press=self.metni_degistir)
        duzen.add_widget(self.dugme)
        return duzen
        
olayUyg().run()    
