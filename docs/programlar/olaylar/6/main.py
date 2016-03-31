from kivy.app import App
from kivy.uix.popup import Popup

class PopUpPencere(Popup):

    def olayDugme(self, uyg):
        ad=self.ids.girilen_ad.text
        uyg.root.ids.ana_pencere_etiket.text="Merhaba %s !" % ad
        self.dismiss()

class olayUyg(App):

    def popAc(self):
        self.popup=PopUpPencere()
        self.popup.open()

olayUyg().run()
