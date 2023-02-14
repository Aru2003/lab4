print("Enter number a and b:")
a, b = input(), input()
while not(a.isdigit() and b.isdigit()):
    a, b = input(), input()
print("Summa :")
print(int(a) + int(b))