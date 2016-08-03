# -*- coding: utf-8 -*-

from kivy.app import App

from xml.etree import ElementTree
agac = ElementTree.parse('Il-ilce-Semt-Mahalle-PostaKodu.xml')  
xmlKok = agac.getroot()

class illerIlceler(App):

    def argCevir(self, satir, nesne):
        return {'text': nesne["adi"], 'size_hint_y': None, 'height': 25} 

    def ilSecim(self, nesne):
        if nesne.selection:
            secim=nesne.selection[0].index
            ilId=nesne.data[secim]['ilId']

            ilceler=xmlKok.findall('tbl_ilce')
        
            self.root.ids.ilceler.adapter.data= [
                                    {'ilceId': ilce.find('ilce_id').text, 'adi': ilce.find('ilce_ad').text.encode("utf-8")}
                                    for ilce in ilceler if ilce.find('il_id').text==ilId
                                ]

            self.root.ids.ilceler._trigger_reset_populate()

    def ilceSecim(self, nesne):
        if nesne.selection:
            secim=nesne.selection[0].index
            ilceId=nesne.data[secim]['ilceId']

            semtler=xmlKok.findall('tbl_semt')
        
            self.root.ids.semtler.adapter.data= [
                        {'semtId': semt.find('semt_id').text, 'adi': semt.find('semt_ad').text.encode("utf-8")} 
                        for semt in semtler if semt.find('ilce_id').text==ilceId
                    ]

            self.root.ids.semtler._trigger_reset_populate()

    def build(self):

        iller=xmlKok.findall('tbl_il')

        self.root.ids.iller.adapter.data= [ 
                        {'ilId': il.find('il_id').text, 'adi': il.find('il_ad').text.encode("utf-8")}
                        for il in iller 
                    ]

        self.root.ids.iller.adapter.bind(on_selection_change=self.ilSecim)
        self.root.ids.ilceler.adapter.bind(on_selection_change=self.ilceSecim)
    
illerIlceler().run()
