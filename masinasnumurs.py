import os
os.system('cls')
print("\n")

skaitli = input("Ievadi skaitļus no 1-9999: ")
burti = input("Ievadi 2 burtus: ")
numurs = burti + skaitli
if (numurs):
    print(f"Numura zīme '{numurs}' ir derīga.")
else:
    print(f"Numura zīme '{numurs}' nav derīga.")