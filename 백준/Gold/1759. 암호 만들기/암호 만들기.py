L, C = map(int, input().split())
alpabets = list(input().split())
# 알파벳이 증가하는 순서로..
alpabets.sort()
# 최소 1개의 모음 / 최소 2개의 자음
# 증가하는 순으로
def check(arr: list[str]):
    모음, 자음 = 0, 0
    for x in arr:
        if x in 'aeiou':
            모음 += 1
        else:
            자음 += 1
    if 모음 >= 1 and 자음 >=2:
        return True
    return False
# 
ans = []
used = [0] * C
def dfs(level, idx):
    if level == L:
        if check(ans):
            print(''.join(ans))
        return
    
    for i in range(idx, C):
        if used[i] == 0:
            used[i] = 1
            ans.append(alpabets[i])
            # 저번에도 i 대신에 idx 넣어서 틀렸는데..또 이 실수?
            dfs(level + 1, i + 1)
            ans.pop()
            used[i] = 0
        

dfs(0, 0)