# https://www.acmicpc.net/problem/10597
# 1<= len(num) <= 50
# 123456789 -> 9자리
# 101112..19 -> 20자리
# 2021....29 -> 20자리
# 따라서 N의 범위 1<= N <= 29(49자리)
# num을 이루고 있던 10진수들은 한 자리 또는 두 자리, 29가 max인 상황
# 1<= len(num) <= 9 : 1 ~ 9까지만 존재
# 10<= len(num) = 9 + 2 * ( N - 9 )

kriii = input()

if len(kriii) <= 9:
    max_num = len(kriii)
else:
    max_num = (len(kriii) + 9) // 2
# --숫자체크
used = [0] * (max_num + 1)
# -- 방문한 노드 값 저장
visited = []

def dfs(idx, kriii):
    if idx == len(kriii):
        print(*visited)
        exit()
    
    # dfs -> 자리수 1개 체크
    num = int(kriii[idx:idx+1])
    if 1<= num <= max_num and used[num] == 0:
        used[num] = 1
        visited.append(num)
        dfs(idx + 1, kriii)
        visited.pop()
        used[num] = 0
        
    if idx + 1 < len(kriii):
        num = int(kriii[idx:idx+2])
        if 1<= num <= max_num and used[num] == 0:
            used[num] = 1
            visited.append(num)
            dfs(idx + 2, kriii)
            visited.pop()
            used[num] = 0
        
dfs(0, kriii)