# -*- coding: utf-8 -*-

import os, sys
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.popup import Popup

class farkliKaydetForm(Popup):
    pass


class metinDuzenleyici(App):



    def farkliKaydetDialog(self):
        form = farkliKaydetForm()
        form.open()

    def farkliKaydetSecim(self, form):
        secilen_dosya=form.ids.dosya_secim.selection
        if secilen_dosya:
            if len(secilen_dosya)>0:
                dosyaAdi=os.path.split(secilen_dosya[0])[1]
                form.ids.dosya_adi.text=dosyaAdi

    def farkiKaydetIslevi(self, form):
        self.son_patika=form.ids.dosya_secim.path
        self.son_dosya=form.ids.dosya_adi.text
        self.dosyaKaydet()
        
    
    def dosyaKaydet(self):
        if not self.son_dosya:
            self.hataGoster("Dosya adı verdiğinizden eminmisiniz?")
        else:
            try:
                dosya_tam_isim = os.path.join(self.son_patika, self.son_dosya)
                F=open(dosya_tam_isim, 'w')
                F.write(self.root.ids.metin.text)
                F.close()
            except:
                self.hataGoster("Dosyayı yazamadım. Nedeni: [color=#FF0000]%s[/color]"
                                 % str(sys.exc_info()[1][1]))

    
    
    def hataGoster(self, hata):
        icerik=Label(text=hata, markup=True)
        popup = Popup(title='Yapamadım !', content=icerik)
        popup.size_hint = (0.7,0.7)
        icerik.bind(on_touch_down=popup.dismiss)
        popup.open()

    def dosyaKaydetIslevi(self):
        if self.son_dosya: self.dosyaKaydet()
        else: self.farkliKaydetDialog()

    def build(self):
        self.son_patika= os.getcwd()
        self.son_dosya=''
        
        
metinDuzenleyici().run()
