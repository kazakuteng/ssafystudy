N, M = map(int, input().split())
def a(num1, num2):
    if num2 == 0:
        return num1
    else:
        return a(num2, num1%num2)

c = a(N, M)
print(c)
print(N*M//c)