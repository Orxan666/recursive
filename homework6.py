# 1. `ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']` şəklində fermaya sahib bir fermer bizdən bəzi köməkliklər istəyir. Fermerə kömək etmək üçün aşağıdakı tapşırıqları yerinə yetirin.
#     1. Fermada keçinin sırasını tapın
#     2. Fermadakı heyvanları ad sırasına görə sıralayın
#     3. Fermadan bir at çıxarıb, ən sağdan bir toyuq əlavə edin
#     4. Ən soldan bir keci əlavə edin
#     5. Fermanın yarısını dinamik bir şəkildə silin
# 2. Yeni gələn `['at', 'qoyun', 'inek', 'inek', 'qoyun']` heyvanları fermaya əlavə edin
#     1. Fermadakı heyvanları 3 qatına çıxarın
#     2. Fermadakı heyvanları tərsinə sıralayın
#     3. Fermadakı ineklerin sayının ümumi fermanın neçə faizi olduğunu tapın
#     4. Oxşar fermadan istəyən basqa bir fermerə fermamızın kopyasını verin
#     5. Fermada təmir işi getməlidi, heyvanları çölə çıxarmaq üçün fermanı təmizləyin

ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']


# print(ferma.index("keci"))
# ferma.sort()
# ferma.remove("at") 
# ferma.append("toyuq")
# ferma.insert( 0,'keci')

# del ferma[:len(ferma)//2]

    # 1. Fermadakı heyvanları 3 qatına çıxarın
    # 2. Yeni gələn `['at', 'qoyun', 'inek', 'inek', 'qoyun']` heyvanları fermaya əlavə edin
    # 3. Fermadakı heyvanları tərsinə sıralayın
    # 4. Fermadakı ineklerin sayının ümumi fermanın neçə faizi olduğunu tapın
    # 5. Oxşar fermadan istəyən basqa bir fermerə fermamızın kopyasını verin
    # 6. Fermada təmir işi getməlidi, heyvanları çölə çıxarmaq üçün fermanı təmizləyin



# ferma2=['at', 'qoyun', 'inek', 'inek', 'qoyun']
# ferma=ferma*3
# ferma.extend(ferma2)



# print(ferma)

# ferma.reverse()
# print(ferma)

# count=ferma.count("at")
# print(((count)/len(ferma))*100)
# print(ferma.count("at")/len(ferma)*100)

# print(ferma.copy())

# ferma.clear()n

# print(ferma)

# result = [0,0]
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]

# for i in numbers:
#     if i>0:
#         result[0]+=i
#     else:
#         result[1]+=i

# print(result)

# a=5
# b=4
# b=a
# print(b)

# reqemler=input("Reqem daxil edin")
# myList=[]

# for item in reqemler:
#     if int((item))%2==1:
#         myList.append(item)
#     myList.reverse()
# print(myList)


# ballar = [31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]

# kesilen_telebe = 0
# successfull_student = 0
# yuksek_netice=[]
# for i in ballar:
#     if i < 51:
#         kesilen_telebe += 1
#     elif i>80:
#         yuksek_netice.append(i)
#     else:
#         successfull_student += 1

# print("Kəsilən tələbə sayı:", kesilen_telebe)
# print("Uğurlu tələbə sayı:", successfull_student)
# print("80 baldan yuxari yiganlar",yuksek_netice)

# cem = 0
# for i in ballar:
#     cem += i

# ortalama = cem / len(ballar)
# print("Ortalama:", ortalama)

# reng=input("Reng daxil ein: ")

# if reng=="qirmizi":
#     print("Dayan")
# elif reng=="sari":
#     print("Hazirlas")
# elif reng=="yasil":
#     print("Basla")
# else:
#     print("Daxil etdiyiniz yoxdur")



# ---------------------------------------------

# Dictionary task

# users = [
#     {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
#     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
#     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# ]


# user_name=input("Istifadeci adini daxil edin: ")
# password=input("Siferinizi daxil edin: ")

# user_found=False

# finded_user=None

# for user in users:
#     if user["username"]==user_name:
#         finded_user=user_name
#         user_found=True
#         if user.password==password:
#             if user['blocked']:
#                 print("Istifadeci bloklanib")
#             else:
#                 print(user["name"],"xos geldiniz")
#         else:
#             print("Istifadeci parolu yanlisdir")


# 1. İstifadəçinin boyunu 1sm artırın
# 2. Telefonun markasını dəyişərək Samsung edin
# 3. İstifadəçinin adını silin
# 4. İstifadəçinin ilk sifarişini silin
# 5. İstifadəçinin sifarişlərinin əvvəlinə ball əlavə edin
# 6. Sonuna headphones əlavə edin

user = { 
    'name': 'Elnur',
    'height': 179,
    'phone': {
        'model': 'Iphone',
    },
    'orders': ['book', 'mouse', 'mousepad']
}

# user['height']+=1
# user["phone"]["model"]="samsung"
# del user["name"]

# user.clear()
# del user ["orders"][0]o
# user["orders"].insert(0,"ball")

# print(user)

# user["orders"].append("headphones")

# print(user)


# 3. `info = ["Resul", "Serifov", 35]`
#     1. Yuxarıdakı arrayı dinamik olaraq `["Resul Serifov", 25]` vəziyyətinə gətirin


# info = ["Resul", "Serifov", 35]

# info=" ".join(info[:2]),25

# print(info)


shop = {
    "t-shirt": 59.00,
    "jeans": 75.00,
    "sweatshirt": 60.00,
    "shoes": 124.99,
    "jacket": 154.90
}

# productName = input("Mehsul adini daxil edin: ")

# searchProductName = None

# for key, value in shop.items():
#     if key == productName:
#         searchProductName = value

# if searchProductName is None:
#     print("Mehsul tapilmadi")
# else:
#     print(searchProductName)


# shop.update({'ball':70,'siqaret':50.2})

# print(shop)

# print(len(shop))

# for key,value in shop.items():
#     shop[key]=value*1.3

# print(shop)

# myList=[1,2,3,4,5,6]

# for i in myList:
#     if i%2==0:
#         print(i)

# result=[i for i in myList if i%2==0]
# print(result)

# myList=[1,2,3,4,5,6,7,8]

# new_list=[ x**3 for x in myList if x%2==1]
# print(new_list)


# miriList=[i for i in range(1,100) if i%2==0]
# print(miriList)

# new_dic = {i:i**2 for i in range(1,11)}


# print(new_dic)

