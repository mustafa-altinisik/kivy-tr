# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button

class olayUyg(App):

    def metni_degistir(self, nesne):
        nesne.text='Tıkladın ve değiştim.'

    def build(self):
        dugme=Button(text='Değiştir')
        dugme.bind(on_press=self.metni_degistir)
        return dugme
        
olayUyg().run()    
