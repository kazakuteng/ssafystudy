N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

points.append(points[0])  # 마지막 -> 처음 연결

a = 0
b = 0

for i in range(N):
    a += points[i][0] * points[i+1][1]
    b += points[i][1] * points[i+1][0]

area = abs(a - b) / 2

print(f"{area:.1f}")