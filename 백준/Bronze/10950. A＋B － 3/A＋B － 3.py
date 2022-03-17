T = int(input())
for i in range(1, T+1) :
    if 1<= i <= T :
        A, B = map(int, input().split())
    else :
        break
    print(A+B)