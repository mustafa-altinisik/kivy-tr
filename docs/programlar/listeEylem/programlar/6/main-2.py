# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from kivy.uix.actionbar import ActionBar
from kivy.uix.actionbar import ActionView
from kivy.uix.actionbar import ActionButton
from kivy.uix.actionbar import  ActionPrevious

class eylemCubugu(App):

    def build(self):
    
        eylemcubugu= ActionBar(pos_hint= {'top':1})

        eylemgorunumu=ActionView()
        eylemcubugu.add_widget(eylemgorunumu)

        oncekieylem=ActionPrevious(title='Eylem Çubuğu', app_icon='document-edit.png')
        eylemgorunumu.add_widget(oncekieylem)
        
        duzen = BoxLayout(orientation='vertical')
        duzen.add_widget(eylemcubugu)

        self.etiket=Label(text="Ana Alan")
        duzen.add_widget(self.etiket)
        
        return duzen

eylemCubugu().run()
