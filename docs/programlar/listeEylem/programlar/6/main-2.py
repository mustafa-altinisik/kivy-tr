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

        #oncekieylem=ActionPrevious(title='Eylem Çubuğu', app_icon='document-edit.png')
        #oncekieylem=ActionPrevious(title='Eylem Çubuğu', app_icon='atlas://data/images/defaulttheme/close')
        oncekieylem=ActionPrevious(title='Eylem Çubuğu', app_icon='atlas://atlasim/document-edit')
        eylemgorunumu.add_widget(oncekieylem)
        
        aksiyondugmesi2=ActionButton(icon='atlas://atlasim/document-open')
        eylemgorunumu.add_widget(aksiyondugmesi2)
        

        
        aksiyondugmesi1=ActionButton(icon='atlas://atlasim/document-save')
        eylemgorunumu.add_widget(aksiyondugmesi1)
        

        aksiyondugmesi4=ActionButton(icon='atlas://atlasim/document-save-as')
        eylemgorunumu.add_widget(aksiyondugmesi4)
        
        
        
        aksiyondugmesi3=ActionButton(icon='atlas://atlasim/document-new')
        eylemgorunumu.add_widget(aksiyondugmesi3)

        aksiyondugmesi5=ActionButton(icon='atlas://atlasim/application-exit')
        eylemgorunumu.add_widget(aksiyondugmesi5)

        
        duzen = BoxLayout(orientation='vertical')
        duzen.add_widget(eylemcubugu)

        self.etiket=Label(text="Ana Alan")
        duzen.add_widget(self.etiket)
        
        return duzen

eylemCubugu().run()
