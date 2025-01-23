from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from datetime import datetime
from kivy.uix.stencilview import StencilView


class Appnote(BoxLayout,StencilView):
    pass
    

class Myapp(App):
    def build(self):
        return Appnote()
    
    def add_activity(self, activity_text, date_text, time_text):
        if not activity_text:
            return  # ถ้าไม่มีข้อความ activity ให้ return ออกไปเลย
        activity_layout = self.root.ids.activity_layout
        new_activity = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40)
        new_activity.add_widget(Label(text=activity_text, size_hint=(0.7, 1)))
        activity_layout.add_widget(new_activity, index=0)  # เพิ่มข้อความใหม่ด้านบน
        
        # ตั้งเวลาและเสียงเตือน
    #     self.set_alarm(date_text, time_text, activity_text)
    
    # def set_alarm(self, date_text, time_text, activity_text):
    #     try:
    #         alarm_time = datetime.strptime(f"{date_text} {time_text}", "%Y-%m-%d %H:%M")
    #         # โค้ดสำหรับตั้งเวลาและเสียงเตือนจะถูกเพิ่มที่นี่
    #     except ValueError:
    #         print("รูปแบบวันที่หรือเวลาไม่ถูกต้อง")

if __name__ == '__main__':
    Myapp().run()

