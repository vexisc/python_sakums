import os
os.system('cls')

txt = int(input("Cik tev ir gadu? "))

if txt <= 7:
    print("Biļete bez maksas.")
if 7 <= txt <= 18:
    print ("Biļete maksā 5 eiro.")
if 18 <= txt <= 65:
    print ("Biļete maksā 10 eiro.")
if txt > 65:
    print ("Biļete maksā 3 eiro.")