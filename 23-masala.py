# for va range dan foydalanish
# for yordamida 1 dan 10 gacha solarni chiqarish
'''sonlar=[1,2,3,4,5,6,7,8,9,10]
kunlar=['Du','Se','CHor','Pa','Ju','shan','yak']
for son in sonlar:
    print(son)
for kun in kunlar:
    print(kun)'''
'''#range bilan ishlash
# 0 dan 9 sonlar
for son in range(12):
    print(son)'''
'''# 0 dan 9 sonlar
for son in range(10,21,2):
        print(son)'''
'''# 2 dan 19 sonlar orasidagi 3 qadam bilan chiqarish
for son in range(2,19,3):
        print(son)'''
'''# 1 dan 10 gach bo'lgan sonlar orasidan faqat 7-raqami chiqmasin
for i in range(1,10):
    if i==7:
        continue
    print(i)'''
'''# 1 dan 10 gach bo'lgan sonlar orasidan faqat 7 va 9-raqami chiqmasin
for i in range(1,11):
    if i==7 or i==9:
        continue
    print(i)'''
'''# 1 dan 30 gach bo'lgan sonlar orasidan faqat 18 dan 22 gacha chiqmasin
for i in range(1,31):
    if i>=18 and i<=22:
        continue
    print(i)'''
'''# 
for i in range(1,101):
    if i%5==0 or i%10==0 :
        continue
    print(i)'''
'''# 1 dan 100 gacha bo'lgan sonlarni kirting lekin oxiri 0,1,2,3,4,5 bilan tugaydigan ikki xonali sonlar chiqmasin
for son in range(1, 101):
    if son % 10 <= 5 and son // 10 > 0:
        continue
    print(son)'''
'''a=int(input("a="))
b=int(input("b="))
if a<b:
    for a in range(a,b):
        print(a)
else:
    for a in range(a,b,-1):
        print(a)'''