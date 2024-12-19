import os
os.system('cls')
print("\n")

#def hello(kam):
#    print("hello ", kam)


#name = input("Kā tevi sauc?")
#hello(name)

def main():
    x = int(input("x - ?"))
    print("x kvadrātā ir", kvadrats(x))

def kvadrats(n):
    return n * n