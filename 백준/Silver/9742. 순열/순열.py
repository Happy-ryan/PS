# https://www.acmicpc.net/problem/9742

def dfs(level, n):
    global cnt
    if level == n:
        cnt += 1
        if cnt == int(k):
            print(''.join(ans))
        return
    
    for i in range(len(s)):
        if used[i] == 0:
            used[i] = 1
            ans.append(s[i])
            dfs(level + 1, n)
            ans.pop()
            used[i] = 0

while True:
    try:
        s, k = input().split()
        k = int(k)
        
        max_val = 1
        for i in range(1, len(s) + 1):
            max_val *= i
            
        ans = []
        used = [0] * len(s)
        cnt = 0
        if k > max_val:
            print(f"{s} {k} = No permutation")
        else:
            print(f"{s} {k} = ", end="")
            dfs(0, len(s))
        
    except:
        break