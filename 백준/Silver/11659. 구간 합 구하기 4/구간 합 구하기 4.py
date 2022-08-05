n,m = map(int,input().split())
arr = [0]+list(map(int,input().split()))
brr = [list(map(int,input().split())) for _ in range(m)]

# 누적합
dp =[0]*(n+1)
for i in range(1,n+1):
    dp[i] = arr[i] + dp[i-1]

# 특정 구간의 합 = [구간누적합-구간누적합]빼기로 접근하자!
def f(a,b):
    sum = dp[b] - dp[a-1]
    return sum
for row in brr:
    print(f(row[0],row[1]))