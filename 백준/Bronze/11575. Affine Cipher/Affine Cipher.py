def solution(A, B, message):
    mod = 26
    answer = ''
    conv = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for idx,x in enumerate(message):
        num = (A * conv.find(x) + B) % mod
        message[idx] = conv[num]
        
    return ''.join(message)

t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    message = list(input())
    print(solution(A, B, message))