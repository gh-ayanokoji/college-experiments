bin = int(input("Enter Binary Number: "))

decimal = 0
base = 1

while bin!= 0:
    decimal += (bin % 10) * base
    base *= 2
    bin //= 10

print(decimal)