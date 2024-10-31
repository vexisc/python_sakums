import os
os.system('cls')

import math

a = float(input("Ieraksti skaitli! "))
b = float(input("Ieraksti otro skaitli! "))
c = float(input("Ieraksti trešo skaitli! "))

d = (b**2)-(4*a*c)



if d > 0:
    x = (((-b) + math.sqrt(d))/2*a)
    s = (((-b) - math.sqrt(d))/2*a) 
    print("Saknes ir", x, "un", s)
if d == 0: 
    f = (-b / 2*a)
    print("Sakne ir", x)
if d < 0:
    print("Nav sakņu.")