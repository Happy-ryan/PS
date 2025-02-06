n = int(input())
X, S = map(int, input().split())
weas = [list(map(int, input().split())) for _ in range(n)]
weas.sort(key= lambda x: (-x[1], x[0])) # 공격력은 쎄고 가격은 쌀수록 좋고

p = 0
for price, powewr in weas:
    if price <= X:
        p += powewr
        X -= price
        break
    
if p > S:
    print('YES')
else:
    print('NO')