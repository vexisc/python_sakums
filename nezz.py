import os
os.system('cls')

#1

for num in range(1, 10000):
    summa = 0
    for i in range (1, num):
        if num % i == 0:
            summa = summa + i
    if summa == num:
        print(f"{num} ir perfekts skaitlis")

#2

n = int(input("Ievadiet skaitli n: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end="") 
        j += 1
    print() 
    i += 1

#3
print("Pirmie 15 Fibonači virknes skaitļi")
b = 15
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= b:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()

#4
print("Viens līdz simts")
for number in range(100):
    print(number + 1)