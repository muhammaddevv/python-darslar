# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:03:13 2023

@author: user
"""
# #1
# dadam = {'name':'SHuxrat',
#          't_yili':1965,
#          'location':'tashkent'}

# print(f"otamning ismi {dadam['name']}, dadam {dadam['t_yili']} yilda tug\'ilgan, hozirda dadam {dadam['location'].title()} da yashaydi")

# # 2
# oilam = {'dadam':'palov','onam':'xonim','akam':'shashlik','akam2':'baliq','ayolim':'qozon_kabob'}
# taom = oilam['dadam']
# taom_2 = oilam['onam']
# taom_3 = oilam['akam']
# print(f"dadamning sevimli taomi {taom}, onamning sevimli taomi {taom_2}, akamning sevimli taomi esa {taom_3}")


# 3

# py_dict = {'string':'matn',
#            'integer':'son',
#            'float':'o\'nlik son',
#            'title':'bosh_katta',
#            'print':'chop_etish',
#            'list':'ro\'yhat'}
# print(py_dict['float'])


# 4 

python_izohli_lugati = {'string':'matn',
           'integer':'son',
           'float':'o\'nlik son',
           'title':'bosh_katta',
           'print':'chop_etish',
           'list':'ro\'yhat'}

# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")





















