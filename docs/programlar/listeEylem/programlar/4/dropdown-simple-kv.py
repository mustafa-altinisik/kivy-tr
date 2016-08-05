# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.lang import Builder

kv='''
BoxLayout:    
    Button:
        id: anadugme
        text: "Başlat"
        on_release: app.acilirkutu.open(self)
        size_hint: (None, None)
'''

class acilirKutuKv(App):

    def secim(self, nesne):
        self.acilirkutu.select(nesne.text)
        self.root.ids.anadugme.text=nesne.text

    def build(self):
        self.root=Builder.load_string(kv)
        self.acilirkutu = DropDown()

        for x in ( "Mustafa", "Dilek", "Fatih", "Melike"):
            dugme=Button(text=x, size_hint_y=None, height=25)
            dugme.bind(on_release=self.secim)
            self.acilirkutu.add_widget(dugme)

        return self.root

acilirKutuKv().run()
