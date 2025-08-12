C, K, P = map(int, input().split())

val = 0
for i in range(1, C + 1):    
    val += K * i + P * (i ** 2)
    
print(val)