t = int(input())

for  _ in range(t):
    g, c, e = map(int, input().split())
    
    required_candies = e - c
    
    if g == 1:
        required_km = required_candies
    elif g == 2:
        required_km = 3 * required_candies
    elif g == 3:
        required_km = 5 * required_candies
    else:
        print("Invalid group")
        continue

    if required_candies <= 0:
        print("0")
    else:
        print(f"{required_km}")