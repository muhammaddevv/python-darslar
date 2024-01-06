def toliq_ism_yasa(ism, familiya):
    """to'liq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism
talaba = toliq_ism_yasa("muhammad", "sheraxanov")
print(talaba)

def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    """to'liq ism qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()
talaba_1 = toliq_ism_yasa("muhammad", "sheraxanov", "shuxratovich")
talaba_2 = toliq_ism_yasa("zarnigor", "sheraxanova")
print(f"darsga kelmagan talabalar {talaba_1} va {talaba_2}")


def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    """avtolar haqida info"""
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yili':yili,
            'narh':narhi}
    return avto
avto1 = avto_info('gm', 'lacetti', 'qora', 'avtomat', 2022)
avto2 = avto_info('kIA', 'KIA K5', 'kulrang', 'gibrid', 2021, 35000)
avtolar = [avto1, avto2]
print('onlayn bozordagi mashinalar')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = 'nomalum'
    print(f"{avto['rang']} {avto['model']} , narhi: {narh}")


def oraliq(start, stop, qadam=1):
    """range funksiyasi"""
    sonlar = []
    while start < stop:
        sonlar.append(start)
        start += qadam
    return sonlar
print(oraliq(10, 21, 2))




def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    """avtolar haqida info"""
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yili':yili,
            'narh':narhi}
    return avto

avtolar = []
while True:
    print("Quyidagi ma'lumotlarni kiriting",end='')
    kompaniya = input("\nIshlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narhi: ")
    # foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
    # lug'at shakllantirib , har bir lug'atni ro'yxatga qo'shamiz
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob == 'no':
        break

print("\nSalonimizdagi avtolar:")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi {narh}")
