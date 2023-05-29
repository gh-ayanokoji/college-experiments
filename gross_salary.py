basic = int(input("Enter your basic salary: "))

HRA = (10*basic)/100
TA = (5*basic)/100
gross = basic+HRA+TA

Ptax = (2*gross)/100

net = gross-Ptax
print("Net Gross Salary is", net)