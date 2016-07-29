# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.listview import ListView
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton


class kitaplarUyg(App):

    def argumanCevirici(self, satir, nesne):
        return {'text': nesne["adi"], 'size_hint_y': None, 'height': 25} 

    def build(self):
    
        kitaplar=[ {'adi':'Python', 'yazari':'Mustafa Başer', 'yayinevi':'Dikeyeksen'},
                   {'adi':'Ruby', 'yazari':'Timur Karaçay', 'yayinevi':'Seçkin'},
                   {'adi':'Perl-CGI', 'yazari':'Rıza Çelik', 'yayinevi':'Seçkin'},
                   {'adi':'Php', 'yazari':'Mehmet Şamlı', 'yayinevi':'Kodlab'} ]
        
        liste_adaptoru=ListAdapter(args_converter=self.argumanCevirici,
                                   data=kitaplar,
                                   cls=ListItemButton,
                                   allow_empty_selection=False)
        
        listeGorunumu=ListView(adapter=liste_adaptoru)
        
        return listeGorunumu
      
kitaplarUyg().run()
    
