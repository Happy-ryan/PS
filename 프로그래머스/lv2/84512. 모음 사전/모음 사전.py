
arr = [ 'A', 'E', 'I', 'O', 'U']
visted = []
final = []
def dfs(lev, M):
    if lev == M:
        final.append(''.join(visted))
        return
    for i in range(len(arr)):
        visted.append(arr[i])
        dfs( lev + 1, M)
        visted.pop()

for m in range(1, 6):
    dfs(0, m)
    
def solution(word):
    answer = sorted(final).index(word) + 1
    return answer