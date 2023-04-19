#같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
#같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
#모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  

def f(a, b, c):
    sum_val = 0
    if (a == b) and (b == c) and (a == c):
        sum_val += 10000
        sum_val += a * 1000
    elif (a != b) and (a != c) and (b != c):
        sum_val += max(a, b, c) * 100
    else:
        sum_val += 1000
        if a == b and a != c: # a, b
            sum_val += a * 100
        elif b == c and a != c: # b, c
            sum_val += b * 100
        else: #a, c
            sum_val += a * 100
    return sum_val


t = int(input())
ans = 0
for _ in range(t):
    a, b, c = map(int, input().split())
    ans = max(ans, f(a, b, c))
    
print(ans)
        