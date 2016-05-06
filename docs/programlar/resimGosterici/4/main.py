# -*- coding: utf-8 -*-

import os, imghdr
from kivy.app import App
from kivy.uix.image import Image

class resimGosterici(App):

    def resimleriEkle(self, dosyalar):
        for dosya in dosyalar:
            if imghdr.what(dosya):
                resim=Image(source=dosya)
                self.root.ids.karinca.add_widget(resim)

    def build(self):
        self.son_patika=os.getcwd()
        dosyalar=[ os.path.join(self.son_patika, x) for x in os.listdir(self.son_patika) ]
        self.resimleriEkle(dosyalar)

resimGosterici().run()
