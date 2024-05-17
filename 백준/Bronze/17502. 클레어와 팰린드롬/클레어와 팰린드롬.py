n = int(input())
s = list(input())

def solution(n, s):
    
    if n % 2 != 0 and s[n // 2] == '?':
        s[n // 2] = 'x'
        
    for idx in range(len(s) // 2):
        if s[idx] == '?' and s[n - idx - 1] != '?':
            s[idx] = s[n - idx - 1]
        elif s[idx] != '?' and s[n - idx - 1] == '?':
            s[n - idx - 1] = s[idx]
        elif s[idx] == '?' and s[n - idx - 1] == '?':
            s[idx] = s[n - idx - 1] = 'a'
            
    return ''.join(s)

print(solution(n, s))