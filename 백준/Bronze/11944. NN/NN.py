n,m = map(int,input().split())
s =""
for _ in range(n):
    s += str(n)

if len(s) >= m:
    print(s[:m])
else:
    print(s)