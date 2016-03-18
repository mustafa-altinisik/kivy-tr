import kivy

from kivy.app import App
from kivy.uix.label import Label

class BenimUygulamam(App):

    def build(self):
        return Label(text='Merhaba Dünya!')


BenimUygulamam().run()
