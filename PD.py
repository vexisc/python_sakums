import os
os.system('cls')
print("\n")

#1
a = input("Ievadi tekstu: ")

print(a[-5:])

#2

cip = int(input("Ievadiet skaitli: "))
b = 0

for i in range(cip, cip + 20): 
    if cip % 3 == 0:
        continue
    print (cip)
    b += 1
    print (b)
    if b == 15:
        break
#3

sk = int(input("Ievadiet sakuma skaitli: "))

sksr = [sk - i for i in range (10)]

for sk in sksr:
    print (sk)

print("Saraksta garums", len(sksr))

#4

dictionary = {
    "Anna": 20, 
    "Jānis": 22, 
    "Ilze": 19,
    "Zane": 17,
}

vards = input("Ieraksti vārdu, kādu vēlies meklēt(pieejami Anna, Jānis, Ilze, Zane): ")

if vards in dictionary:
    print(f"{vards} ir {dictionary[vards]} gadus vecs/a.")
else:
    print("Nav atrasts/a.")

#5

import time

sec = int(input("Ievadiet sekundes:"))

for remain in time.time (sec, -1, -1):
    min = remain // 60
    sec = remain % 60

print(f" {min: 02} : {sec: 02} ")
time.sleep(1)

print("Kontroldarbs beidzies!")