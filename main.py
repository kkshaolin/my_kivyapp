from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from datetime import datetime

class Appnote(BoxLayout):
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
        self.root.ids.activity_input.text = ''
        self.root.ids.date_input.text = ''
        self.root.ids.time_input.text = ''
        
        # ตั้งเวลาและเสียงเตือน
        self.set_alarm(date_text, time_text, activity_text)
    
    def set_alarm(self, date_text, time_text, activity_text):
        try:
            alarm_time = datetime.strptime(f"{date_text} {time_text}", "%Y-%m-%d %H:%M")
            current_time = datetime.now()
            time_diff = (alarm_time - current_time).total_seconds()
            if time_diff > 0:
                Clock.schedule_once(lambda dt: self.play_alarm(activity_text), time_diff)
            else:
                print("The specified time is in the past.")
        except ValueError:
            self.root.ids.date_input.text = 'Invalid date/time'
    
    def play_alarm(self, activity_text):
        sound = SoundLoader.load('alarm.wav')
        if sound:
            sound.play()
        print(f"Alarm for activity: {activity_text}")
    
 
if __name__ == "__main__":
    Myapp().run()