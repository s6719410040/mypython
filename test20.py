emp_id = input("ป้อนรหัสพนักงาน: ")
emp_name = input("ป้อนชื่อพนักงาน: ")
sales = float(input("ป้อนยอดขาย: "))
if sales <= 1000:
    commission = 0.0
elif sales <= 2000:
    commission = sales * 0.01
elif sales <= 3000:
    commission = sales * 0.03
else:
    commission = sales * 0.05
print(f"รหัส: {emp_id} ชื่อ: {emp_name} ยอดขาย: {sales:.2f} บาท")
print(f"ค่าคอมมิชชั่น: {commission:.2f} บาท")
