# def miri():
#     print("Salam Miri")


# miri()



# def topla(*args):
#     return sum(args)


# print(topla(2,4,8))

# ad="Ferid"
# soyad="Ceferov"
# print(ad,soyad,"xos gelmisen")
# print(f"{ad} {soyad} xos geldiniz")

# myDic={
#     "name":"Fero",
#     "age":70,
#     "hobby":"Swimming"
# }

# def menimfunksiyam(**kwargs):
#     return list(kwargs.items())


# print(menimfunksiyam(**myDic))


# def test(firstName):
#     return firstName.upper()




# test=lambda firstName:firstName.upper()

# print(test("Subhan"))



# def greet(firstName,lastName):
#     # return firstName,lastName,"xos geldiniz"
#     return f"{firstName} {lastName} xos geldiniz"

# print(greet("Miri","Soltanov"))




# ad="Murad"
# soyad="Nesirli"
# yas=19

# print(f"{ad} {soyad} {yas}")


# def bolme(a,b,c):
#     return a%b%c

# print(bolme(227,9,3))

# def test():
#     pass


# import math

# print(math.pi)


# def cut(*args):
#     return (sum(i) for i in args if i%2==0)
# print(cut(4,6,7,8))



# print(type(15j))



# def test(x):
#     if x%2==0:
#         return "cutdur"
#     else:
#         return "tekdir"

# print(test(15))

# import timeit



# myList=[1,2,3,4,5,6,7,8,9]

# tek_eded_yoxlayan_func=lambda elxan:["tekdir" if i%2==1 else "cutdur" for i in elxan] 


# def tek_eded_yoxlayan_funksiya(elxan):
#     for i in elxan:
#         if i%2==1:
#             return "tekdir"
#         else:
#             return "cutdur"


# print(timeit.timeit(lambda:tek_eded_yoxlayan_func(myList),number=100))
# print(timeit.timeit(lambda:tek_eded_yoxlayan_funksiya(myList),number=100))


# print(tek_eded_yoxlayan_funksiya(myList))



# tek_eded_yoxlayan_func=lambda elxan: [i for i in elxan if i%2==1]

# print(tek_eded_yoxlayan_func(myList))

# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)

# print(factorial(9))


# import math
# print(math.factorial(5))



# print(abs(-20))

# firstName=-2
# print(len(firstName))
# print(bool(firstName))


print(dir(__builtins__))