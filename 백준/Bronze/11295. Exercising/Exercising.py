num = 1

while True:
    L = int(input())
    if L == 0:
        break

    N = int(input())

    print(f"User {num}")
    num += 1

    for _ in range(N):
        steps = int(input())
        d = L * steps / 100000 
        print(f"{d:.5f}")