# การทำงานของ Code

การทำงานจะมี 2 ไฟล์คือไฟล์ main.py และ myapp.kv

## main.py

  จะเริ่มจากนำเข้าโมดูลที่จะใช้ในการสร้าง App จากนั้นสร้าง class Appnote ซึ่งจะอธิบายการทำงานในส่วนของการทำงานในไฟล์ myapp.kv ส่วนอีก class ที่ถูกสร้างใน main.py คือ class Myapp ที่เป็น class ที่ใช้ในการ run ที่สืบทอดมาจาก โมดูล App และได้เขียนฟังก์ชันใน class ด้วยกัน 4 ฟังก์ชัน เริ่มจาก
  
  1.function build ที่ใช้สำหรับหน้า UI ที่ return class Appnote ที่เป็นโครงสร้างของหน้าแอพพลิเคชั่น และได้สร้าง list เก็บกิจกรรมที่มีการกดเช็ค
  
  2.function add_activity ใช้สำหรับสร้างข้อความจากที่ผู้ใช้ป้อนมา เริ่มทำงานโดย เช็คข้อความถ้าไม่มีให้ return ออก แล้วจากนั้น อ้างถึง id (activity_layout) ของ BoxLayout ทีจะใช้เก็บข้อความ และสร้าง BoxLayout สร้าง Label แล้วเพิ่ม Label ใน BoxLayout สร้าง chack box ตั้งค่าให้เรียกฟังก์ชัน on_checkbox_active เมื่อกดติก เพิ่มเช็คบล็อกใน BoxLayout เพิ่ม BoxLayout ใน BoxLayout ที่มี id:activity_layout และลบข้อความในช่อง input

  3.function on_checkbox_active ทำงานโดยตรวจสอบว่าผู้ใช้กดเช็คบล็อกไม่ ถ้ากดจะเพิ่มกิจกรรมใน list ใน function build และ ลบข้อความใน BoxLayout ที่มี id:activity_layout

  4.function show_history ทำงานโดย สร้าง ScrollView และ Boxlayout แล้วเพิ่มกิจกรรมที่กดติกใน Boxlayout เพิ่ม Boxlayout ใน ScrollView และสร้างปุ่มปิดหน้า Popup หลังจากนั้น สร้าง Popup ชื่อ History และเพิ่ม ScrollView และปุ่มปิดเข้าไป 

## myapp.ky

ใช้ในการออกแบบหน้า UI ดั่งนี้

    <Appnote>: เป็น root widget ของแอปพลิเคชัน
        BoxLayout : เลย์เอาต์หลักที่จัดเรียงในแนวตั้ง

    BoxLayout:
    
        Label: แสดงชื่อแอพพลิเคชั่น   
    BoxLayout:
    
        BoxLayout (box name goal): แสดงข้อความ "Goal" ด้วยฟอนต์และขนาดที่กำหนด
        
        BoxLayout (box goal 2): ใช้แสดงเป้าหมายระยะสั้นและระยะยาว
        
          Label: แสดงข้อความ "Short term:" และ "Long-term:"
          
          TextInput: รับข้อความเป้าหมายระยะสั้นและระยะยาวจากผู้ใช้
          
          CheckBox: ให้ผู้ใช้ติ๊กเพื่อทำเครื่องหมายว่าเป้าหมายเสร็จสิ้นแล้ว
          
    BoxLayout: ใช้แสดงกิจกรรม (Activity) ของผู้ใช้

        Label: แสดงข้อความ "Activity"
        
        Button: ปุ่ม History สำหรับกดดูรายการที่กดติ้ก
        
        ScrollView: ใช้สำหรับเลื่อนดูรายการกิจกรรมที่เพิ่มเข้ามา
        
            BoxLayout : ใช้เก็บข้อความที่ผู้ใช้ป้อน
            
        BoxLayout: ใช้สำหรับเพิ่มกิจกรรมใหม่
        
            TextInput: รับข้อความกิจกรรมจากผู้ใช้
            
            Button: สำหรับกดเพิ่มกิจกรรมใหม่


# การรันและภาพรวม

แอพนี้ประกอบด้วย 2 ส่วนหลักๆ คือ goal ที่ผู้ใช้สามารถป้อนเป้าหมายของตนเองลงไปแบ่งเป็นเป้าหมายระยะสั่นและเป้าหมายระยะยาว อีกส่วนคือ activity ที่ให้ผู้ใช้ใส่กิจกรรมที่ต้องทำลงไปแล้วเมื่อทำสำเร็จแล้วกดติ้กข้อความจะหายไป แล้วสามารถดูประวัติกิจกรรมที่ทำสำเร็จได้ด้วย
