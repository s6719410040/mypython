# คำสั่ง break, continue
#break ใน loop ทำงานเมื่อใดจบ loop ทันที
#continue ใน loop ทำงานเมื่อใดจบ Loop แต่รอบนั้นทันที แล้วไปเริ่มรอบใหม่เลย

for aa in range(5):
    if aa == 2:
        break
    print(aa, "Hello...")
print("++++++++++++++++++++++++++++++++")
for aa in range(5):
    if aa == 2:
        continue
    print(aa, "Hello...")