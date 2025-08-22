# การใช้ 1 print() มีข้อมูลหลายประเภททำไง????? มี 4 วิธี
print('Hello', 555, 'wow', 999, True, 'Hi', 10 + 20 -5, 152.875)

# วิธีที่ 2 ใช้ + (ข้อมูลไหนที่ไม่ใช้ sting ต้องทำให้เป็น sting ใช้ฟังชั่น str())
# 
print('hello'+str(555)+'wow'+str(999)+str(True)+'Hi'+str(10 + 20 - 5)+str(152.875))
print('hello'+str(555)+'wow'+str(999)+str(True)+'Hi'+str(10 + 20 - 5)+str(152.875))


print('Hello {} Wow {} {} Hi {} {}' .format(555,999,True,10+20-5,152.875))

print('{4} {2}' . format('a', 'b', 'c', 'd', 'e'))

print(f'Hello {555} Wow {999} {True} Hi {10 + 20 - 5} {152.875}')