cnt = 1

while True:
    a, b, c = map(int, input().split())
    
    if a == b == c == 0:
        break
    
    if cnt > 1:
        print()
    print(f"Triangle #{cnt}")

    if c == -1:
        print(f"c = {((a ** 2 + b ** 2) ** 0.5):.3f}")
    elif max(a, b) >= c:
        print("Impossible.")
    elif a == -1:
        print(f"a = {((c ** 2 - b ** 2) ** 0.5):.3f}")
    elif b == -1:
        print(f"b = {((c ** 2 - a ** 2) ** 0.5):.3f}")  
    cnt += 1