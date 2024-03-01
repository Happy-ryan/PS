n = int(input())
words = [input() for _ in range(n)]

def check(word):
    dic = {}
    for idx, w in enumerate(word):
        if w not in dic:
            dic[w] = str(idx)
    
    ans = ''
    for w in word:
        ans += dic[w]
        
    return ans
        
def solution(n, words):
    
    step = []
    cnt = 0
    def dfs(level, start):
        nonlocal cnt
        if level == 2:
            if check(step[0]) == check(step[1]):
                cnt += 1
            return
        
        for idx in range(start, n):
            step.append(words[idx])
            dfs(level + 1, idx + 1)
            step.pop()
        
    dfs(0, 0)
    
    return cnt

print(solution(n, words))