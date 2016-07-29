# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class kitaplarUyg(App):

    def secim(self, nesne):
        if nesne.selection:
            secimID=nesne.selection[0].index
            secilenKitap=nesne.data[secimID]

            icerik=Label(text='Kitap Adı: %s\nYazarı: %s\nYayınevi: %s' % (
                              secilenKitap['adi'],
                              secilenKitap['yazari'],
                              secilenKitap['yayinevi']))
        
            popup = Popup(title='Seçilen Kitap',
                          content=icerik,
                          size_hint=(None, None), size=(200, 150))

            icerik.bind(on_touch_down=popup.dismiss)
            popup.open()

    def argumanCevirici(self, satir, nesne):
        return {'text': nesne["adi"], 'size_hint_y': None, 'height': 25} 

    def build(self):
    
        kitaplar=[ {'adi':'Python', 'yazari':'Mustafa Başer', 'yayinevi':'Dikeyeksen'},
                   {'adi':'Ruby', 'yazari':'Timur Karaçay', 'yayinevi':'Seçkin'},
                   {'adi':'Perl-CGI', 'yazari':'Rıza Çelik', 'yayinevi':'Seçkin'},
                   {'adi':'Php', 'yazari':'Mehmet Şamlı', 'yayinevi':'Kodlab'} ]
        
        self.root.ids.kitaplar.adapter.data=kitaplar
        
        self.root.ids.kitaplar.adapter.bind(on_selection_change=self.secim)

        
kitaplarUyg().run()    
