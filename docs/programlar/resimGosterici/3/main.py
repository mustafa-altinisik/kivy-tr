# -*- coding: utf-8 -*-

import os, imghdr
from kivy.app import App
from kivy.uix.image import Image

class resimGosterici(App):

    def build(self):
        self.son_patika=os.getcwd()
        for dosya in os.listdir(self.son_patika):
            if imghdr.what(dosya):
                resim=Image(source=dosya)
                self.root.ids.karinca.add_widget(resim)

resimGosterici().run()
