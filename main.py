from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Appnote(BoxLayout):
    pass
    

class Myapp(App):
    def build(self):
        return Appnote()
    
    def add_activity(self, activity_text):
        if activity_text:
            activity_layout = self.root.ids.activity_layout
            new_activity = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40)
            new_activity.add_widget(Label(text=activity_text, size_hint=(1, 1)))
            activity_layout.add_widget(new_activity, index=0)  # เพิ่มข้อความใหม่ด้านบน
            self.root.ids.activity_input.text = ''
    
 
if __name__ == "__main__":
    Myapp().run()