# https://www.acmicpc.net/problem/1174
# 가장 큰 수 9876543210 - 10자리
# 그 이상은 존재 불가..

def dfs(level, idx, n):
    global cnt
    if level == n:
        res.append(int(''.join(map(str,ans.copy()))))
        cnt += 1
        return
    for i in range(idx, 10):
        ans.append(numbers[i])
        # 나보다 인덱스가 무조건 큰 것만 고르는 백트래킹인 경우!!
        # level + 1될 때 현재 인덱스 + 1 하기!
        dfs(level + 1, i + 1, n)
        ans.pop()
# 전체 경우의 수 1023개
sum_val = 0   
numbers = [9,8,7,6,5,4,3,2,1,0] 
res = []
for i in range(1, 11):
    cnt = 0
    ans = []
    dfs(0, 0, i)
    sum_val += cnt    

res.sort()
n = int(input())
if sum_val < n:
    print(-1)
else:
    print(res[n - 1])