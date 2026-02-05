N, X = map(int, input().split())
a = list(map(int, input().split()))
total = []
people = 0
for i, j in enumerate(a):
    people += j
    if i >= X-1:
        total.append(people)
        people -= a[i-X+1]
if max(total) == 0:
    print("SAD")
else:
    print(max(total))
    print(total.count(max(total)))