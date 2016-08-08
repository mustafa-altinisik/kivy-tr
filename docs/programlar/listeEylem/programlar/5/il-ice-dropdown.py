# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

import sqlite3
sqlbaglantisi = sqlite3.connect('iller.db')
isaretci = sqlbaglantisi.cursor()

class illerIlcelerAcilirKutu(App):

    def secimIl(self, nesne):
        if self.iller.secim: 
            self.iller.secim.background_color=1, 1, 1, 1
        
        self.iller.secim=nesne
        self.iller.select(nesne.text)
        self.root.ids.iller.text="Seçilen İl: %s" % nesne.text
        nesne.background_color= 1, 0, 0, 1

        self.ilceler.clear_widgets()
        self.semtler.clear_widgets()
        self.root.ids.ilceler.text="İlçe Seçiniz"
        self.root.ids.semtler.text="Semt Seçiniz"
       
        isaretci.execute('SELECT ilce_id, ilce_ad FROM tbl_ilce WHERE il_id=%d' % nesne.il_id)
        for ilce in isaretci.fetchall():
            dugme=Button(text=ilce[1].encode("utf-8"), size_hint_y=None, height=25)
            dugme.ilce_id=ilce[0]
            dugme.bind(on_release=self.secimIlce)
            self.ilceler.add_widget(dugme)

    def secimIlce(self, nesne):
    
        if self.ilceler.secim: 
            self.ilceler.secim.background_color=1, 1, 1, 1

        self.ilceler.secim=nesne
        self.ilceler.select(nesne)
        self.root.ids.ilceler.text="Seçilen İlçe: %s" % nesne.text
        nesne.background_color= 1, 0, 0, 1
        
        self.semtler.clear_widgets()
        self.root.ids.semtler.text="Semt Seçiniz"

        isaretci.execute('SELECT semt_id, semt_ad FROM tbl_semt WHERE ilce_id=%d' % nesne.ilce_id)
        for semt in isaretci.fetchall():
            dugme=Button(text=semt[1].encode("utf-8"), size_hint_y=None, height=25)
            dugme.semt_id=semt[0]
            dugme.bind(on_release=self.secimSemt)
            self.semtler.add_widget(dugme)
        
    def secimSemt(self, nesne):
        if self.semtler.secim: 
            self.semtler.secim.background_color=1, 1, 1, 1

        self.semtler.secim=nesne
        self.semtler.select(nesne)
        self.root.ids.semtler.text="Seçilen Semt: %s" % nesne.text
        nesne.background_color= 1, 0, 0, 1

    def build(self):
        self.iller = DropDown()
        self.iller.secim=None
        isaretci.execute('SELECT il_id, il_ad FROM tbl_il')
        for il in isaretci.fetchall():
            dugme=Button(text=il[1].encode("utf-8"), size_hint_y=None, height=25)
            dugme.il_id=il[0]
            dugme.bind(on_release=self.secimIl)
            self.iller.add_widget(dugme)

        self.ilceler = DropDown()
        self.ilceler.secim=None
        self.semtler = DropDown()
        self.semtler.secim=None

illerIlcelerAcilirKutu().run()
