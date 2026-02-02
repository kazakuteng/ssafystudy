list1 = []
for i in range(10):
    list1.append(int(input()))
list2 = [0 for i in range(42)]
for i in list1:
    list2[i%42] = 1

c = 0
for i in list2:
    if i:
        c += 1
print(c)