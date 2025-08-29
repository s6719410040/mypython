#โปรแกรมคำนวณราคาสินค้าที่รับส่วนลดแล้ว โดยป้อนรหัสสินค้า ชื่อสินค้า ประเภทสินค้า ซึ่งมี 4 ประเภท คือ food(F/f), woman(W/w), man(M/m), kitchen(K/k) โดยป้อนเป็นตัวย่อ  และราคาสินค้าทางแป้นพิมพ์ แล้วคำนวณราคาสินค้าที่รับส่วนลดแล้วทางหน้าจอ โดยสินค้าประเภท food ลด 2% ของราคาสินค้า, woman ลด 4% ของราคาสินค้า, man ลด 6% ของราคาสินค้า, kitchen ลด 10% ของราคาสินค้า หากป้อนประเภทสินค้าผิดจากที่กำหนดให้แสดงข้อความ "คุณป้อนประเภทผิด !!!"
 
print("------------------")
print("โปรแกรมคํานวณราคาสินค้า")
print("------------------")
product_code = input("กรุณาป้อนรหัสสินค้า : ")
product_name = input("กรุณาป้อนชื่อสินค้า : ")
product_type = input("กรุณาป้อนประเภทสินค้า (F/f, W/w, M/m, K/k): ")
product_price = float(input("กรุณาป้อนราคาสินค้า : "))
print("------------------")
if product_type == "F" or product_type == "f":
   pro_salary = product_price * 0.02
   print(f"ราคาสินค้าลดแล้วเป็น{pro_salary}บาท")
elif product_type == "W" or product_type == "w":
   pro_salary = product_price * 0.04
   print(f"ราคาสินค้าลดแล้วเป็น{pro_salary}บาท")
elif product_type == "M" or product_type == "m":
   pro_salary = product_price * 0.06
   print(f"ราคาสินค้าลดแล้วเป็น{pro_salary}บาท")
elif product_type == "K" or product_type == "k":
   pro_salary = product_price * 0.10
   print(f"ราคาสินค้าลดแล้วเป็น{pro_salary}บาท")
else:
   print("คุณป้อนประเภทผิด !!!")
print("------------------")