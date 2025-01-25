from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.stencilview import StencilView
from kivy.uix.checkbox import CheckBox

class Appnote(BoxLayout, StencilView):
    pass

class Myapp(App):
    def build(self):
        return Appnote()
    
    def add_activity(self, activity_text):
        if not activity_text:
            return  # ถ้าไม่มีข้อความ activity ให้ return ออกไปเลย
        activity_layout = self.root.ids.activity_layout
        new_activity = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40)
        new_activity.add_widget(Label(text=activity_text, size_hint=(0.7, 1), font_name='font/THSarabunNew.ttf', font_size=20))
        
        # เพิ่ม CheckBox และตั้งค่า event listener
        checkbox = CheckBox(size_hint=(0.3, 1))
        checkbox.bind(active=lambda instance, value: self.remove_activity(new_activity) if value else None)
        new_activity.add_widget(checkbox)
        
        activity_layout.add_widget(new_activity, index=0)  # เพิ่มข้อความใหม่ด้านบน
        
        # ล้างข้อความใน TextInput
        self.root.ids.activity_input.text = ''
    
    def remove_activity(self, activity_widget):
        activity_layout = self.root.ids.activity_layout
        activity_layout.remove_widget(activity_widget)

if __name__ == '__main__':
    Myapp().run()