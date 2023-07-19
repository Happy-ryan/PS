# 가격, 무게
s = list(map(int, input().split()))
n = list(map(int, input().split()))
u = list(map(int, input().split()))
# 가성비 계산
def solution(weight, price):
    total = 0
    if price * 10 >= 5000:
        total = price * 10 - 500
    else:
        total = price * 10
    ws = weight * 10
    
    return ws / total

ans = [("S", solution(s[1], s[0])),
       ("N", solution(n[1], n[ 0])),
       ("U", solution(u[1], u[0]))]

ans.sort(key= lambda x: x[1], reverse=True)

print(ans[0][0])