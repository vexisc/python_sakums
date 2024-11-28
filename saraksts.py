import os
os.system('cls')
print("\n")

skolens = ["Vikotrija", "Artūrs", "Džošua", "Roberts"]
#print(skolens)

#print(skolens[1])
#print(skolens[2])
#print(skolens[0])

#for sk in skolens:
#    print(sk)

#skola = "25. vidusskola"
#for burts in skola:
#    print(burts)

#for i in range(len(skolens)):
#    print(i + 1, skolens[i])

#skolotajs = ["Gustava", "Ungure", "Deksne", "Gladčenko"]
#macibu_prieksmets = ["matemātika", "matemātika", "matemātika", "fizika"]

#skolotajs = {
#            "Gustava":  "matemātika",
#            "Ungure": "matemātika",
#            "Deksne": "matemātika",
#            "Gladčenko": "fizika",
#}

#print (skolotajs["Deksne"])
#print (skolotajs["Gladčenko"])

#for skol in skolotajs:
#    print(skol, skolotajs[skol], sep = " māca ")

#skolotajs = [
#    {"uzvards": "Gustava", "mācību priekšmets": "matemātika", "kabinets": "27."}
#    {"uzvards": "Deksne", "mācību priekšmets": "matemātika", "kabinets": None}
#]
#for skol in skolotajs:
#    print(skol["uzvards"], skol["mācību priekšmets"], skol['kabinets'])

platums = int(input("platums- "))
augstums = int(input("augstums- "))

for i in range(augstums):
    for j in range(platums):
        print("@", end="")
    print()
    