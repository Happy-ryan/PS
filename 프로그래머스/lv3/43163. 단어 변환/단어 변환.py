def f(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]: cnt += 1
    return cnt

def solution(begin, target, words):
    answer = 100
    visited = ['']
    final = []
    used = [0] * len(words)
    
    def dfs(begin, words):
        global answer
        if visited[-1] == target:
            a = visited.copy()
            final.append(len(a) - 1)
            return
        
        for i, word in enumerate(words):
            if used[i] == 0 and f(word, begin) == 1:
                used[i] = 1
                visited.append(word)
                dfs(word, words)
                visited.pop()
                used[i] = 0

    dfs(begin, words)      
    
    if len(final) == 0:
        return 0
    else:
        return min(final)