#โปรแกรมซึ่งรับชื่อ และปีเกิดของผู้ใช้โปรแกรมทางแป้นพิมพ์ โดยหากอายุที่ผู้ใช้ป้อนมีค่าตั้งแต่ 35 ปีขึ้นไป ให้แสดงข้อความว่า "คุณแก่แล้ว..." หากไม่ถึงให้แสดงข้อความ "คุณยังไม่แก่..." ทางหน้าจอ

from datetime import datetime

print("------------------")
print("โปรแกรมตรวจสอบปีเกิด")
print("------------------")
your_name = input("กรุณาป้อนชื่อของคุณ : ")
your_yearbirth = input("กรุณาป้อนปีเกิดของคุณ : ")
print("------------------")

your_yearbirth = (datetime.now().year+543)  - your_yearbirth

if your_yearbirth >= 35:
    print(f"คุณ {your_name} อายุ {your_yearbirth} คุณแก่แล้ว...")
else:
    print(f"คุณ {your_name} อายุ {your_yearbirth} คุณยังไม่แก่...")
print("------------------")