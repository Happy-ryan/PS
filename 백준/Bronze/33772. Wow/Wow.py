n = int(input())
words = [input() for _ in range(2)]

def solution(n, words):
    up = words[0]
    
    w = '\\../\\../'
    v = '\\../'
    
    ans = ''
    idx = 0

    while idx < len(up):
        
        if up[idx : idx + 8] == w:
            ans += 'w'
            idx += 8
        elif up[idx : idx + 4] == v:
            ans += 'v'
            idx += 4
        elif up[idx] == '.':
            idx += 1
        
    return ans

    
    
print(solution(n, words))