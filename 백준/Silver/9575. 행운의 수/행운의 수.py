def f(a, b, c):
    flag = True
    k = a + b + c
    for x in str(k):
        if x in ['0', '1','2','3','4','6','7','9']:
            flag = False
    return flag

t = int(input())
for _ in range(t):
    cnt = set()
    a = int(input())
    A = list(map(int, input().split()))
    b = int(input())
    B = list(map(int, input().split()))
    c = int(input())
    C = list(map(int, input().split()))
    for a1 in A:
        for b1 in B:
            for c1 in C:
                if f(a1, b1, c1):
                    cnt.add(a1 + b1+ c1)
    print(len(cnt))