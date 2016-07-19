# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.clock import Clock

class kronometre(App):
        
    def etiketteGoster(self):
        self.root.ids.ana_etiket.text="%s:%s.%s" % (self.dakika,
                                                    str(self.saniye).zfill(2),
                                                    str(self.salise).zfill(2)
                                                    )
    def zamanlayiciIslevi(self, za):
        self.salise +=1
        self.etiketteGoster()
        if self.salise==10:
            self.salise=0
            self.saniye +=1
        if self.saniye==60:
            self.saniye=0
            self.dakika +=1

    def sifirla(self):
        self.salise=0
        self.saniye=0
        self.dakika=0
        self.etiketteGoster()
        
    def baslat(self):
        if self.root.ids.baslat_dugme.text=="Başlat":
            Clock.schedule_interval(self.zamanlayiciIslevi, 0.1)
            self.root.ids.baslat_dugme.text="Durdur"
        else:
            Clock.unschedule(self.zamanlayiciIslevi)
            self.root.ids.baslat_dugme.text="Başlat"

    def build(self):
        self.sifirla()
        
kronometre().run()
