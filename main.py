# #zad1
# lista = ["piłka nożna", "koszykówka", "siatkówka"]
# lista.reverse()
# lista.extend(["bieg na 1000", "biegi przełajowe"])
# print(lista)
#zad2
# slownik = {"np": "na przykład", "cd": "ciąg dalszy", "itp": "i tym podobne "}
# print(slownik)
#zad3
# slownik = {"wiedzmin": "rpg", "gothic": "rpg", "age of empires": "strategia"}
# print(slownik)
#zad4
# napis = input("podaj napis")
# print(napis.count("a"))
#zad5
#
# system.stdout.write("podaj a\n")
# a=int(system.stdin.readline())
# system.stdout.write("podaj b\n")
# b=int(system.stdin.readline())
# system.stdout.write("podaj c\n")
# c=int(system.stdin.readline())
#
#
# dzialanie = a**b+c
# print((dzialanie))
#zad6
# a = int(input("Podaj a"))
# b = int(input("Podaj b"))
# c = int(input("Podaj c"))
#
# if (a >= b) & (a >= c):
#     print(a)
# elif (b >= a) & (b >= c):
#     print(b)
# else:
#     print(c)
#zad7
# lista = [1, 2.5, 7, 4.14]
# for x in range (0, len(lista), 1):
#     lista[x] *= lista[x]
# print(lista)
#zad8
# lista=[]
# count = 0
# while count <=9:
#     a = int(input("Podaj liczbe"))
#     count+=1
#     if a % 2 == 0 :
#         lista.append(a)
# print(lista)
#zad9
# napis = ""
# lista = [1, 2, 3 ,4 ,5]
# for x in lista:
#     if x%2 == 0:
#         napis+="E\n"
#     else:
#         napis+="EEEEEE\n"
# print(napis)
# Zad10

# x = (input("Podaj x aby obliczyc sqrt(x)"))
#
# try:
#         wynik = math.sqrt(int(x))
#         print(wynik)
# except ValueError:
#         print("Podano ujemny x")
