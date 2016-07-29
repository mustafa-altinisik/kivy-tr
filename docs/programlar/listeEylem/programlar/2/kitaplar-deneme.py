# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.listview import ListView
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton


class kitaplarUyg(App):

    def argumanCevirici(self, satir, nesne):
        return {'text': '%s (%s)' % (nesne["adi"], nesne['yazari']),
               'size_hint_y': None, 'height': 25,
               'deselected_color': [1,1,0,1],
               'selected_color': [1,0,1,1]
               } 

    def build(self):
    
        kitaplar=[ {'adi':'Python', 'yazari':'Mustafa Başer', 'yayinevi':'Dikeyeksen'},
                   {'adi':'Ruby', 'yazari':'Timur Karaçay', 'yayinevi':'Seçkin'},
                   {'adi':'Perl-CGI', 'yazari':'Rıza Çelik', 'yayinevi':'Seçkin'},
                   {'adi':'Php', 'yazari':'Mehmet Şamlı', 'yayinevi':'Kodlab'} ]
        
        liste_adaptoru=ListAdapter(args_converter=lambda satir, nesne:{'text':nesne["adi"],'size_hint_y': None, 'height': 25},
                                   data=kitaplar,
                                   cls=ListItemButton,
                                   allow_empty_selection=False)
        
        listeGorunumu=ListView(adapter=liste_adaptoru)
        
        return listeGorunumu
      
kitaplarUyg().run()
    
