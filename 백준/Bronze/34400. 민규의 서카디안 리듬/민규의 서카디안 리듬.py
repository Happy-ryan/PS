T = int(input())

for _ in range(T):
    t = int(input())
    if t % 25 < 17:
        print("ONLINE")
    else:
        print("OFFLINE")