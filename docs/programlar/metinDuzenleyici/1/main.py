from kivy.app import App
from kivy.uix.popup import Popup

class dosyaAcForm(Popup):
    pass

class metinDuzenleyici(App):

    def metinSec(self):
        self.root.ids.metin.select_text(5,15)
        
        
    def dosyaAcDialog(self):
        self.dosya_ac=dosyaAcForm()
        self.dosya_ac.open()

    def dosya_yukle(self, dosya):
        if dosya:
            self.root.ids.metin.text = open(dosya[0]).read()
        self.dosya_ac.dismiss()
        
            

    def build(self):
        self.son_patika = '.'
        
        
        
        
metinDuzenleyici().run()  
