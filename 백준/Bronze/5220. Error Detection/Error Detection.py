t = int(input())

for _ in range(t):
    num, check = map(int, input().split())
    
    ones = bin(num).count('1')
    
    if ones % 2 == check:
        print("Valid")
    else:
        print("Corrupt")