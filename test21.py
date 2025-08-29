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
