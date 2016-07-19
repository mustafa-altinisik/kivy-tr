# -*- coding: utf-8 -*-

import os, imghdr
import sys
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.clock import Clock

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
    
        if self.root.ids.karinca.slides:
            self.root.ids.slyat_dugme.disabled=False
        else:
            self.root.ids.slyat_dugme.disabled=True

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
        
    def zamanlayiciIslevi(self, za):
        self.root.ids.karinca.load_next()
        
    def slaytGosterisi(self, kok):
        if kok.ids.slyat_dugme.text=="Slaytı Başlat":
            Clock.schedule_interval(self.zamanlayiciIslevi, 1)
            kok.ids.slyat_dugme.text="Slaytı Durdur"
        else:
            Clock.unschedule(self.zamanlayiciIslevi)
            kok.ids.slyat_dugme.text="Slaytı Başlat"

    def build(self):
        self.root.ids.karinca.loop=True
        self.son_patika=os.getcwd()
        
                
        # Aşağıdaki satırlar bölüm içerisinde anlatılmadı. Bu satırlar sayesinde program
        # çalıştırılırken argüman olarak verilen klasördeki resimler yüklenir.
        # Örneğin programı komut satırından main.py d:/resimler ile çalıştırırsanız
        # program açıldığında d:/resimler klasöründeki resimler yüklenir. Aksi halde
        # programın çalıştığı klasördeki resimler yüklenir.
        
        if len(sys.argv)>1:
            if os.path.isdir(sys.argv[1]):
                self.son_patika=sys.argv[1]
        
        self.root.ids.slyat_dugme.disabled=True
        dosyalar=[ os.path.join(self.son_patika, x) for x in os.listdir(self.son_patika) ]
        self.resimleriEkle(dosyalar)

resimGosterici().run()
