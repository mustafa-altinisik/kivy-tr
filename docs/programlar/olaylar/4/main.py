# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label
class olayUyg(App):

    def yazdir(self, nesne, deger):
        print deger
        #nesne.text = deger

    def build(self):
        etiket = Label(text='[ref=Selam Melike !] Merhaba  Fatih ![/ref]')
        etiket.markup=True
        etiket.bind(on_ref_press=self.yazdir)
        return etiket

olayUyg().run()
