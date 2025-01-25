from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.stencilview import StencilView
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup

class Appnote(BoxLayout, StencilView):
    pass

class Myapp(App):
    def build(self):
        self.checked_activities = []
        return Appnote()
    
    def add_activity(self, activity_text):
        if not activity_text:
            return  # ถ้าไม่มีข้อความ activity ให้ return ออกไปเลย
        activity_layout = self.root.ids.activity_layout
        new_activity = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40)
        label = Label(text=activity_text, size_hint=(0.7, 1), font_name='font/THSarabunNew.ttf', font_size=20)
        new_activity.add_widget(label)
        
        # เพิ่ม CheckBox และตั้งค่า event listener
        checkbox = CheckBox(size_hint=(0.3, 1))
        checkbox.bind(active=lambda instance, value: self.on_checkbox_active(value, label.text))
        new_activity.add_widget(checkbox)
        
        activity_layout.add_widget(new_activity, index=0)  # เพิ่มข้อความใหม่ด้านบน
        
        # ล้างข้อความใน TextInput
        self.root.ids.activity_input.text = ''
    
    def on_checkbox_active(self, value, activity_text):
        if value:
            self.checked_activities.append(activity_text)
        else:
            self.checked_activities.remove(activity_text)
    
    def remove_activity(self, activity_widget):
        activity_layout = self.root.ids.activity_layout
        activity_layout.remove_widget(activity_widget)
    
    def show_history(self):
        content = BoxLayout(orientation='vertical')
        for activity in self.checked_activities:
            content.add_widget(Label(text=activity, font_name='font/THSarabunNew.ttf', font_size=20))
        popup = Popup(title='History', content=content, size_hint=(0.8, 0.8))
        popup.open()

if __name__ == '__main__':
    Myapp().run()