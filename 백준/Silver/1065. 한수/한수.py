N = int(input())
total = 0
for i in range(1, N+1):
    if i < 100:
        total += 1
    elif i == 1000:
        total = 144
    else:
        if i%10 - (i//10)%10 == (i//10)%10 - i//100:
            total += 1
print(total)