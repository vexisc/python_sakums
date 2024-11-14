import os
os.system('cls')

parole = input("Ievadi paroli! ")
x = parole.isdigit
y = parole.isupper

if len(parole) < 9:
    print("Neatbilst nosacījumiem.")
if y < 1:
    print("Neatbilst nosacījumiem.")
if x < 1:
    print("Neatbilst nosacījumiem.")
elif len(parole) > 9 and y > 1 and x < 1:
    print("Parole atbilst visiem nosacījumiem!")