list1 = [23, 45, 67, 61, 94, 45]
sum = 0
for i in list1:
    sum += i
avg = sum / len(list1)
print(avg)

sum = 0
for i in list1:
    sum += i
print(sum)

max = list1[0]
for i in list1:
    if i > max:
        max = i
print(max)

min = list1[0]
for i in list1:
    if i < min:
        min = i
print(min)