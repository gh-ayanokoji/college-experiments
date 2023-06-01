m1 = int(input("Enter marks of m1: "))
bxe = int(input("Enter marks of bxe: "))
sme = int(input("Enter marks of sme: "))
em = int(input("Enter marks of em: "))
ech = int(input("Enter marks of ech: "))

num = (m1+bxe+sme+em+ech)/5

if num >= 75:
    print("First Class with Distinction")

elif num >= 60:
    print("First Class")

elif num >= 50:
    print("Second Class")

elif num >= 40:
    print("Third Class")

else:
    print("Fail")