n = int(input())
words = [input() for _ in range(n)]

def solution(n, words):
    
    ans = []
    for x in ['keys', 'phone', 'wallet']:
        if x not in words:
            ans.append(x)
    
    if not ans:
        print('ready')
    else:
        for x in ans:
            print(x)

solution(n, words)