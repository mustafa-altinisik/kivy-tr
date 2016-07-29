# -*- coding: utf-8 -*-

from kivy.app import App

class kitaplarUyg(App):

    def argumanCevirici(self, satir, nesne):
        return {'text': nesne["adi"], 'size_hint_y': None, 'height': 25} 

    def build(self):
    
        kitaplar=[ {'adi':'Python', 'yazari':'Mustafa Başer', 'yayinevi':'Dikeyeksen'},
                   {'adi':'Ruby', 'yazari':'Timur Karaçay', 'yayinevi':'Seçkin'},
                   {'adi':'Perl-CGI', 'yazari':'Rıza Çelik', 'yayinevi':'Seçkin'},
                   {'adi':'Php', 'yazari':'Mehmet Şamlı', 'yayinevi':'Kodlab'} ]
        
        self.root.ids.kitaplar.adapter.data=kitaplar
        
kitaplarUyg().run()    
