# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:39:37 2023

@author: user
"""
# 1m
son = int(input('juft son kiriting --> '))
if son % 2:
    print('bu son juf temas')
else:
    print('rahmat')
    


# 2m
mijoz = int(input('yoshingiz nechada? >>> '))

if 4 >= mijoz or mijoz >= 60:
    narh = 0
elif mijoz < 18:
    narh = 10000
else:
    narh = 20000
print(f"chipta {narh} so'm")

# 3m

    
a = float(input("1 chi son kiriting: "))
b = float(input("2 chi son kiriting: "))

if a > b:
    print(f"{a}>{b}")
elif a==b:
    print(f"{a}=={b}")
else:
    print(f"{a}<{b}")

# 4m 

mahsulotlar = ['un', 'kartoshka','piyoz', 'sabzi', 'yog\'', 'sut', 'guruch','mosh' ,'loviya', 'makaron']
savat = []
print('kamida 5 ta mahsulot kiriting')

for i in range(5):
    savat.append(input(f"{i+1} mahsulot nomi "))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"do'konda {mahsulot} bor")
    else:
        print(f"do'konda {mahsulot} yoq")

  # 5 m
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# 6

foydalanuvchilar = ['anvar', 'umar', 'abror', 'samandar', 'baxtiyor', 'davron']
login = input('yangi login tanlang>>> ')

if login.lower() not in foydalanuvchilar:
    print('hush kelibsiz')
else:
    print('login band, yangi login tanlang')


# 7 

son = int(input('butun son kiritng>>> '))
for i in range(2,11):
    if not (son % i):
        print(f"{son} soni {i} ga qoldiqsiz bo\'linadi")
    


son = int(input("Juft son kiriting: "))
if son %2 !=0:
    print("Bu son juft emas.")
else:
    print("Rahmat!")



yosh = int(input("Yoshingiz nechida? >>> "))

if 4 >= yosh or yosh >= 60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")


x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")


mahsulotlar = ['un', "yog", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")    


mahsulotlar = ['un', "yog", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do\'konimizda quyidagi mahsulotlar yo\'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so\'ragan barcha mahsulotlar do\'konimizda bor")
    



users = ['alisher1983','aziza','yasina','umar']

login = input("Yangi login tanlang: ")

if login in users:
    print('Login band, yangi login tanlang!')
else:
    print("Xush kelibsiz!")



son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")






























