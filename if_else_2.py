# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 07:50:18 2023

@author: user
"""

# BOOLEAN darsi

narh = 20000
choy = True
salat = False

if choy and salat:
    narh += 10000
elif choy or salat:
    narh += 5000
print(f"jami narh {narh}")


narh = 20000
choy = True
salat = False
kompot = True
qazi = False
non = True

if choy:
    narh += 3000
    print('mijoz choy oldi')
    
if salat:
    narh += 5000
    print('mijoz salat oldi')

if kompot:
    narh += 4000
    print('mijoz kompot oldi')

if qazi:
    narh += 8000
    print('mijoz qazi oldi')

if non:
    narh += 3000
    print('mijoz non oldi')

print(f"jami narh {narh} bo'ldi")




'' in ''operatori

menu = ['osh', 'manti', 'somsa', 'shashlik', 'norin']
buyurtma = input('nima buyurtma berasiz? --> ')

if buyurtma.lower() in menu:
    print('buyurtma qabul qilindi')
else:
    print('menuda bunday ovqat yo\'q')


menu = ['osh', 'manti', 'somsa', 'shashlik', 'norin']
buyurtma = ['manti', 'lag\'mon', 'norin', 'somsa']
if buyurtma:
    for taom in menu:
        if taom in buyurtma:
            print(f"menuda {taom} bor")
        else:
            print(f"kechirasiz menuda {taom} yo'q")
else:
    print('savatcha bo\'sh')






















