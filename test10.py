# สร้างโปรแกรมรับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้
# และคำนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามา
# เป็นเท่าใด แล้วแสดงผลทางหน้าจอ
# สูตร  
# ผลรวม = เลขตัวที่1 + เลขตัวที่2 + เลขตัวที่3 + เลขตัวที่4 + เลขตัวที่5
# ค่าเฉลี่ย = ผลรวมของเลข 5 จำนวน / 5
 
# ============================
# Program  Average  5  Number
# ============================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================


numbers = []
print('ป้อนตัวเลข 5 ตัว')
for i in range(5):
    number = int(input('ป้อนตัวเลข ' + str(i+1) + ' : '))
    numbers.append(number)


sum_of_numbers = sum(numbers)
average_of_numbers = sum_of_numbers/5



print('=====================================')
print(f"ผลรวมของตัวเลขทั้งหมด 5 ตัว {sum_of_numbers}") 
print(f"ค่าเฉลี่ยของตัวเลขทั้งหมดคือ {average_of_numbers/5}")
print('=====================================')
