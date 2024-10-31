import os
os.system('cls')  # attīra termināla logu pašā sākumā
print("\n")  # ieliek tukšu rindiņu pirms izdrukas

x = int(input("Kāda ir x vērtība? "))
y = int(input("Kāda ir y vērtība? "))

if x < y or x > y:
    print("x nav vienāds ar y")
elif x == y:
    print("x ir vienāds ar y")