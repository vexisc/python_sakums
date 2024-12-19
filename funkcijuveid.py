import os
os.system('cls')
print("\n")


#1 uzd

celsijs = int(input("Ievadi grādus Celsijā! "))

farenhaits = (celsijs * 1.8) + 32
 
print((celsijs, farenhaits))

#2 uzd

a = int(input("Ieraksti skaitli: "))
b = int(input("Ieraksti skaitli: "))
c = int(input("Ieraksti skaitli: "))

sak = a + b + c
beig = sak / 3

 
print("Aritmētiskais vidējais ir ", beig)

#3

def palindroms(s):
    return s == s[::-1]


s = input(f"Ieraksti palindromu: ")
ans = palindroms(s)

if ans:
    print("Vārds ir palindroms")
else:
    print("Vārds nav palindroms")

#4 

d = input("Ievadi skaitli: ")
e = input("Ievadi skaitli: ")
f = input("Ievadi skaitli: ")

skaitli = (d, e, f)
x = max(skaitli)

print("Visaugstākā vēriba no ievadītajām ir", x)

#5

import math

faktorials = int(input("Ievadi skaitli!"))
print("Skaitļa faktoriāls ir", (math.factorial(faktorials)))