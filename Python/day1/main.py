# DAY1

print("hello world")
print(77)
# print() - ekranga matn yoki qiymat chiqarish uchun ishlatiladi

# Variables
name = "Ro'zibek"
age = 22
city = "Tashkent"
print("Ism:", name)
print("Yosh:",age)
print("Shahar:",city)
"""
- O‘zgaruvchi nomi raqam bilan boshlanmaydi.
- Faqat lotin harflari va _ ishlatish mumkin.
- Katta-kichik harflar farq qiladi (name ≠ Name).
"""

#input()- doimo string(matn) qaytaradi.
name = input("Ism: ")
print("Hello",name)

#Agar raqam kiritilsa, uni int() bilan o‘zgartirish kerak:
age = int(input("Yosh: "))
print("Yoshi",age)

#type()
x = 10
y = "Python"
print(type(x))
print(type(y))
"""
<class 'int'>
<class 'str'>
"""



