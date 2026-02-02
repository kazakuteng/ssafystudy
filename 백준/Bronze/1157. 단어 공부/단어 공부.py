a = input()
b = a.upper()

c = [0 for _ in range(26)]
for i in b:
    d = ord(i) - ord('A')
    c[d] += 1
e = max(c)
if c.count(e) > 1:
    print("?")
else:
    print(chr(c.index(e)+ord('A')))