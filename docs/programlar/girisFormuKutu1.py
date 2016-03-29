# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class girisFormu(App):

	def build(self):
	
		duzen = BoxLayout(orientation='vertical')

		duzen.add_widget(Label(text='Kullanıcı Adı:'))
		kullanici_adi = TextInput()
		duzen.add_widget(kullanici_adi)

		duzen.add_widget(Label(text='Parola:'))
		parola = TextInput()
		duzen.add_widget(parola)

		duzen.add_widget(Widget())

		gir_dugme=Button(text='Gir')
		duzen.add_widget(gir_dugme)

		self.title = "Giriş Formu"	

		return duzen

      
girisFormu().run()
