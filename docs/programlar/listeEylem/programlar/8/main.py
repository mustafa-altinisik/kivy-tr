# -*- coding: utf-8 -*-
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', 'False')
import os, sys
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.popup import Popup

class farkliKaydetForm(Popup):
    pass


class dosyaAcForm(Popup):
    pass


class dosyaKaydedilmediForm(Popup):
        pass
class yeniDosyaForm(Popup):
    pass


class cikmadanOnceForm(Popup):
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
                self.metin_degisti=False
                #self.root.ids.cik_dugmesi.background_color = [0, 1, 0, 1]
                self.root.ids.cik_dugmesi.icon='atlas://atlasim/application-exit'
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

    def metinDegisti(self, nesne, deger):
        if self.ilkAcilis: 
            self.ilkAcilis=False
        else: 
            self.metin_degisti=True
            #self.root.ids.cik_dugmesi.background_color = [1, 0, 0, 1]
            self.root.ids.cik_dugmesi.icon='atlas://atlasim/dialog-cancel'
            

    def dosyaAcIsleviDialog(self):
        if self.metin_degisti:
            kaydedilmedi_form = dosyaKaydedilmediForm()
            kaydedilmedi_form.open()
        else:
            self.dosyaAcDialog()
            
    def dosyaAcDialog(self):
        form = dosyaAcForm()
        form.open()
       
       
    def dosyaOku(self, dosya_secim):
       if dosya_secim.selection:
            if len(dosya_secim.selection)>0:
                (self.son_patika,self.son_dosya)=os.path.split(dosya_secim.selection[0])
                try:
                    self.root.ids.metin.text=open(dosya_secim.selection[0]).read()
                    self.root.ids.metin.cursor=self.root.ids.metin.get_cursor_from_index(0)
                    self.metin_degisti=False
                    #self.root.ids.cik_dugmesi.background_color = [0, 1, 0, 1]
                    self.root.ids.cik_dugmesi.icon='atlas://atlasim/application-exit'
                except:
                    self.hataGoster("Dosyayı Okuyamadım. Nedeni: [color=#FF0000]%s[/color]"
                                 % str(sys.exc_info()[1][1]))
       else:
            self.hataGoster("Dosya seçtiğinizden eminmisiniz?")

    def dosyaKayedilmediKaydet(self, kok):
        if self.son_dosya: 
            self.dosyaKaydet()
            kok.dismiss()
            self.dosyaAcDialog()
        else:
            kok.dismiss()
            self.hataGoster("Dosya adı yok. 'Farklı Kaydet' kullanarak kaydetmelisiniz.")

    def yeniDosyaAcIslevi(self):
        if self.metin_degisti:
            form = yeniDosyaForm()
            form.open()
        else:
            self.yeniDosyaAc()
      
    def yeniDosyaAc(self):
        self.root.ids.metin.text=""
        self.son_dosya=''
        #self.root.ids.cik_dugmesi.background_color = [0, 1, 0, 1]
        self.root.ids.cik_dugmesi.icon='atlas://atlasim/application-exit'

    def cik(self):
        if self.metin_degisti:
            kaydedilmedi_form = cikmadanOnceForm()
            kaydedilmedi_form.open()  
        else:
            self.stop()
       
            
    def build(self):
        
        self.son_patika= os.getcwd()
        self.son_dosya=''
        self.root.ids.metin.bind(text=self.metinDegisti)
        self.metin_degisti=False
        #self.root.ids.cik_dugmesi.background_color = [0, 1, 0, 1]
        self.root.ids.cik_dugmesi.icon='atlas://atlasim/application-exit'
        self.ilkAcilis=True
        
        
metinDuzenleyici().run()
