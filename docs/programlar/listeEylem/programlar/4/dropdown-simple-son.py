# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class acilirKutu(App):

    def secim(self, nesne):
        # Önceden seçilmiş bir düğme var ise, arka plan rengini
        # ön tanımlı renge dönüştürelim
        if self.acilirkutu.secim:
            self.acilirkutu.secim.background_color= [1, 1, 1, 1]
            
        self.acilirkutu.select(nesne.text)
        self.anadugme.text=nesne.text
        
        # secim özelliğine yeni nesneyi ekleyelim ve
        # arka plan rengini kırmızı yapalım
        self.acilirkutu.secim=nesne
        nesne.background_color= 1, 0, 0, 1

    def build(self):
        duzen = BoxLayout()
        self.anadugme = Button(text='Başlat', size_hint=(None, None))

        self.acilirkutu = DropDown()
        self.acilirkutu.secim=None
        
        for x in ( "Mustafa", "Dilek", "Fatih", "Melike"):
            dugme=Button(text=x, size_hint_y=None, height=25)
            dugme.bind(on_release=self.secim)
            self.acilirkutu.add_widget(dugme)

        self.anadugme.bind(on_release=self.acilirkutu.open)
        duzen.add_widget(self.anadugme)
 
        return duzen

acilirKutu().run()
