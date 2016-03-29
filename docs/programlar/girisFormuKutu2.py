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
		
		duzen_satir_1 = BoxLayout()
		duzen_satir_1.add_widget(Label(text='Kullanıcı Adı:'))
		kullanici_adi = TextInput()
		duzen_satir_1.add_widget(kullanici_adi)
		duzen.add_widget(duzen_satir_1)

		duzen_satir_2 = BoxLayout()
		duzen_satir_2.add_widget(Label(text='Parola:'))
		parola = TextInput()
		duzen_satir_2.add_widget(parola)
		duzen.add_widget(duzen_satir_2)

		duzen_satir_3 = BoxLayout()
		duzen_satir_3.add_widget(Widget())
		gir_dugme=Button(text='Gir')
		duzen_satir_3.add_widget(gir_dugme)
		
		duzen.add_widget(duzen_satir_3)

		self.title = "Giriş Formu"	

		return duzen

      
girisFormu().run()
