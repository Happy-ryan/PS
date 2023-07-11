t = int(input())
for _ in range(t):
    n = int(input())
    p1 = 0
    p2 = 0
    for _ in range(n):
        f1, f2 = input().split()
        if f1 == f2:
            continue
        # R > S , P > R, S > P
        elif (f1 == 'R' and f2 == 'S') or (f1 == 'P' and f2 == 'R') or (f1 == 'S' and f2 == 'P'):
            p1 += 1
        else:
            p2 += 1
    if p1 > p2:
        print("Player 1")
    elif p1 < p2:
        print("Player 2")
    else:
        print("TIE")