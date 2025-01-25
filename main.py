from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.stencilview import StencilView
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

class Appnote(BoxLayout, StencilView):
    pass

class Myapp(App):
    def build(self):
        self.checked_activities = []  # เก็บกิจกรรมที่ทำเสร็จแล้ว
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
        checkbox.bind(active=lambda instance, value: self.on_checkbox_active(value, new_activity, label.text))
        new_activity.add_widget(checkbox)
        
        activity_layout.add_widget(new_activity, index=0)  # เพิ่มข้อความใหม่ด้านบน
        
        # ล้างข้อความใน TextInput
        self.root.ids.activity_input.text = ''
    
    def on_checkbox_active(self, value, activity_widget, activity_text):
        if value:
            # เพิ่มกิจกรรมที่ทำเสร็จแล้วเข้าไปในประวัติ
            self.checked_activities.append(activity_text)
            
            # ลบกิจกรรมออกจาก Layout
            self.root.ids.activity_layout.remove_widget(activity_widget)
    
    def show_history(self):
        # สร้าง ScrollView
        scroll_view = ScrollView(size_hint=(1, None), size=(400, 400))
        
        # สร้าง content สำหรับเก็บกิจกรรม
        content = BoxLayout(orientation='vertical', size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))  # ตั้งค่าให้ content ขยายตามความสูงของวิดเจ็ตภายใน
        
        # เพิ่มกิจกรรมเข้าไปใน content
        for activity in self.checked_activities:
            activity_label = Label(text=activity, font_name='font/THSarabunNew.ttf', font_size=20, size_hint_y=None, height=40)
            content.add_widget(activity_label)
        
        # เพิ่ม content เข้าไปใน ScrollView
        scroll_view.add_widget(content)
        
        # สร้างปุ่มปิด Popup
        close_button = Button(text="Close", size_hint=(1, 0.1))
        
        # สร้าง Popup และเพิ่ม ScrollView และปุ่มเข้าไป
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(scroll_view)
        popup_content.add_widget(close_button)
        
        popup = Popup(title='History', content=popup_content, size_hint=(0.8, 0.8))
        close_button.bind(on_release=popup.dismiss)  # ปิด Popup เมื่อกดปุ่ม
        
        popup.open()

if __name__ == '__main__':
    Myapp().run()