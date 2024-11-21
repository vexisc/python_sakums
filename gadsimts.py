import os
os.system('cls')

gads = int(input("Ievadi gadu! "))
gadsimts = gads // 100
gad = round(gadsimts, 0)
istais = gad + 1

if gads // 400 or gads //4:
    print(istais,"gadsimts, garais gads")
elif gads // 100:
    print(istais,"gadsimts, īsais gads")
