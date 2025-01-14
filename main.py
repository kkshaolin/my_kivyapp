from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Appnote(BoxLayout):
    pass

class Myapp(App):
    def build(self):
        return Appnote()
 
if __name__ == "__main__":
    Myapp().run()