# 계란이 1개, 사고싶은 사람이 1000명이다.
N, M = map(int, input().split())
price = [int(input()) for _ in range(M)]
price = sorted(price)
max_price = max(price)
sum_price=[]
for num in reversed(range(1,max_price+1)): # 1e6
    cnt = 0
    for x in price: # 1000 -> 1e9
        if num <= x:
            cnt +=1
    ret = min(N,cnt) 
    sum_price.append(num*ret)
sum_price.reverse()
result = max(sum_price)
print(sum_price.index(result)+1, result)