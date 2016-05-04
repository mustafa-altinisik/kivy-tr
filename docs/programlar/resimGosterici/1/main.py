# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label

class atliKarinca(App):

    def build(self):
        karinca = Carousel()
        for i in range(5):
            karinca.add_widget(Label(text="Karınca Sayfası: %d" %i))
            
        return karinca

atliKarinca().run()
