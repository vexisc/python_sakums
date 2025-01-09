from itertools import repeat
import os
os.system('cls')
print("\n")

1#

produkti = {
    'briseles kāposti': 4.4,
    'seleriju saknes': 4.2,
    'brokoļi': 3.0,
    'ziedkāposti': 2.9,
    'burkāni': 2.9,
    'sarkanās bietes': 2.5,
    'salāti': 1.8,
    'upenes': 6.8,
    'avenes': 5.0,
    'zemenes': 4.0,
    'jāņogas': 2.5,
    'āboli': 2.3,
    'apelsīni': 2.2,
    'plūmes': 1.7
}

produkts = input("Ievadiet produktu: ").lower()

if produkts in produkti:
    print(f"Produktā {produkts} balastvielu daudzums uz 100g ir {produkti[produkts]} g.")
else:
    print("Produkts nav dots.")

#2

def bez_patskaniem(a):
    patskani = "aeiouAEIOU"
    result = ""
    for burti in a:
        if burti not in patskani: 
            result += burti
    return result


ievade = input("Ievadi kaut ko: ")

rezultats = bez_patskaniem(ievade)
print("Ievadītais bez patskaņiem:", rezultats)

#3

centi = [5, 10, 20, 50]
summa = 0
while summa < 90:
    c = int(input("Ievieto monētu: "))
    if c in centi:
        summa = summa + c
        print(f"Tagadējā summa ir", summa)
    else:
        print("Ievietota nepareiza monēta.")

if summa == 90:
    print("Atlikums- 0 centi. Paldies!")

if summa > 90:
    atlikums = summa - 90
    print("Jūsu atlikums ir", atlikums, "centi. Paldies!")

#4

def laiks_(laiks):
    stundas, minūtes = laiks.split(":")
    return stundas + minūtes / 60

laiks = input("Ievadīt laiku: ")

stundas = laiks_(laiks)

if 7 <= stundas <= 8:
    print("Ir brokastu laiks.")
if 12 <= stundas <= 13:
    print("Ir pusdienu laiks.")
if 18 <= stundas <= 19:
    print("Ir vakariņu laiks.")