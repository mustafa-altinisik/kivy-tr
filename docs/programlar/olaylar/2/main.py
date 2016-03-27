# -*- coding: utf-8 -*-

from kivy.app import App

class olayUyg(App):

    def metni_degistir(self):
        self.root.ids.dugme.text='Tıkladın ve değiştim.'
        
olayUyg().run()    
