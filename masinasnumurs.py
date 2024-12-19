import os
os.system('cls')
print("\n")

import re

numurs = input("Ievadiet transportlīdzekļa numura zīmi: ").strip().upper()

modelis = r"^[A-PR-UZ]{2}-[1-9]\d{0,3}$"

if re.match(modelis, numurs):
    print(numurs, "numura zīme ir derīga.")
else:
    print(numurs, "numura zīme nav derīga.")