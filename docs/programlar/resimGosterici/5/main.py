# -*- coding: utf-8 -*-

import os, imghdr
import sys
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.popup import Popup

class acForm(Popup):
    pass

class resimGosterici(App):

    def resimleriEkle(self, dosyalar):
        self.root.ids.karinca.clear_widgets()
        for dosya in dosyalar:
            if os.path.isfile(dosya):
                if imghdr.what(dosya):
                    resim=Image(source=dosya)
                    resim.allow_stretch=True
                    resim.keep_ratio=False
                    self.root.ids.karinca.add_widget(resim)


    def klasorAc(self):
        form=acForm()
        form.open()

    def tumResimler(self, kok):
        self.son_patika=kok.ids.dosya_secim.path
        dosyalar=[ os.path.join(self.son_patika, x) for x in os.listdir(self.son_patika) ]
        self.resimleriEkle(dosyalar)

    def secilenResimler(self, kok):
        self.son_patika=kok.ids.dosya_secim.path
        dosyalar=kok.ids.dosya_secim.selection
        self.resimleriEkle(dosyalar)
        

    def build(self):
        self.son_patika=os.getcwd()
        #if len(sys.argv)>1:
        #    if os.path.isdir(sys.argv[1]):
        #        self.son_patika=sys.argv[1]
        
        dosyalar=[ os.path.join(self.son_patika, x) for x in os.listdir(self.son_patika) ]
        self.resimleriEkle(dosyalar)

resimGosterici().run()
