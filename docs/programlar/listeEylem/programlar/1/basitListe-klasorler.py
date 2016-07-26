# -*- coding: utf-8 -*-
from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.lang import Builder

# Note the special nature of indentation in the adapter declaration, where
# the adapter: is on one line, then the value side must be given at one
# level of indentation.

Builder.load_string("""
#:import label kivy.uix.label
#:import sla kivy.adapters.simplelistadapter

<MyListView>:
    ListView:
        adapter:
            sla.SimpleListAdapter(
            data=["Item #{0}".format(i) for i in range(100)],
            cls=label.Label)
""")


class MyListView(BoxLayout):
    pass

if __name__ == '__main__':
    runTouchApp(MyListView())
