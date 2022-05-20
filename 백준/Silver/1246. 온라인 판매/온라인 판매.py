N, M = map(int, input().split())
price = [int(input()) for _ in range(M)]
price = sorted(price)
max_price = max(price)
sum_price=[]
for num in reversed(range(1,max_price+1)): # 1e6
    # for x in price: # 1000 -> 1e9
    #     if num <= x:
    #         cnt +=1 ## 하고싶은것: price 안에 x보다 크거나 같은 것의 개수
    while len(price) and num <= price[-1]:
        price.pop()
    ret = min(N, M - len(price))
    sum_price.append(num*ret)
sum_price.reverse()
result = max(sum_price)
print(sum_price.index(result)+1, result)
