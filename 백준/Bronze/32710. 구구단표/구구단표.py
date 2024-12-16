flag = 0

n = int(input())
for a in range(1, 10):
    if n % a == 0 and n // a <= 9:
        flag = 1
        break
    
print(flag)