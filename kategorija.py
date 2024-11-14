import os
os.system('cls')

skaitlis = int(input("Ievadi skaitli! "))

if skaitlis < 0:
    print("Skaitlis ir negatīvs!")
if skaitlis == 0:
    print("Skaitlis ir nulle!")
if skaitlis > 0:
    print("Skaitlis ir pozitīvs!")

y = 2
pari = int(skaitlis % y)

if pari == 0:
    print("Skaitlis ir pāra.")
if pari == 1:
    print("Skaitlis ir nepāra.")