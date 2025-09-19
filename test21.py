# โปรแกรมแสดงข้อความต้อนรับนักศึกษา โดยรับชื่อ และชั้นปีทางแป้นพิมพ์แล้วแสดงข้อความต้อนรับ ดังนี้

# 	กรณีป้อนชั้นปี 1 แสดงข้อความ "Welcome Freshman"

# 	กรณีป้อนชั้นปี 2 แสดงข้อความ "Welcome Sophomore"

# 	กรณีป้อนชั้นปี 3 แสดงข้อความ "Welcome Junior"

# 	กรณีป้อนชั้นปี 4 แสดงข้อความ "Welcome Senior"

# 	กรณีป้อน ปีอื่นๆ  แสดงข้อความ "Oh, no ...."

student_name = input("ป้อนชื่อนักศึกษา: ")
year = input("ป้อนชั้นปี: ")
if year == "1":
    print(f"Welcome Freshman, {student_name}")
elif year == "2":
    print(f"Welcome Sophomore, {student_name}")
elif year == "3":
    print(f"Welcome Junior, {student_name}")
elif year == "4":
    print(f"Welcome Senior, {student_name}")
else:
    print("Oh, no ....")
