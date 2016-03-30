# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

class olayUyg(App):

    def popAc(self, nesne):
        icerik=Label(text='İşte bir popup')
        
        popup = Popup(title='Popup Pencere Başlığı',
                      content=icerik,
                      size_hint=(None, None), size=(200, 200))

        icerik.bind(on_touch_down=popup.dismiss)
        popup.open()
   
    def build(self):
        return Button(text="Popup için tıkla", on_press=self.popAc)

olayUyg().run()
