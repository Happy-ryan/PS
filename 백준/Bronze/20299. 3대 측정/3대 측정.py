# https://www.acmicpc.net/problem/20299
N, K, L = map(int, input().split())
ratings = [list(map(int, input().split())) for _ in range(N)]

def check(arr):
    
    if sum(arr) < K:
        return False
    
    for x in arr:
        if x < L:
            return False
        
    return True

sum_val = 0
res = []
for idx, rates in enumerate(ratings):
    if check(rates):
        sum_val += 1
        res.append(rates)
        
print(sum_val)
for row in res:
    for x in row:
        print(x, end=' ')