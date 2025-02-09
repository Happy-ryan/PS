t = int(input())

def solution(s, origin):
    
    ans = ''
    for x in s:
        if x == ' ':
            ans += ' '
        else:
            ans += origin[ord(x) - 65]
    
    return ans
    

for _ in range(t):
    s = input()
    origin = input()
    print(solution(s, origin))