

from kivy.app import App

class olayUyg(App):

    def metni_degistir(self):
        girilen_metin = self.root.ids.metin_girdisi.text
        self.root.ids.etiket.text='Merhaba %s !' % girilen_metin
        
olayUyg().run()  
