n = int(input())
transports = dict()

for _ in range(n):
    city, money = input().split()
    transports[city] = int(money)
    
cnt = 0
for c, m in transports.items():
    if m > transports['jinju']:
        cnt += 1
        
print(transports['jinju'])
print(cnt)
