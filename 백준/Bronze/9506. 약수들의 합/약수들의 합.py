while True:
    N = int(input())
    if N == -1:
        break
    a = []
    for i in range(2, N+1):
        if N % i == 0:
            
            a.append(N // i)
    if sum(a) == N:
        print(f'{N} =', end = " ")
        while a:
            print(f'{a.pop()}', end = " ")
            if a:
                print('+', end = " ")
        print("")
    else:
        print(f'{N} is NOT perfect.')