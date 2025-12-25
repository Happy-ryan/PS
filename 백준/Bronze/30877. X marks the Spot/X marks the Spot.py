import sys
input = sys.stdin.readline

N = int(input())
words = [list(input().split()) for _ in range(N)]

def solution(N, words):
    
    answer = ''
    
    S, T = [], []
    
    # 시간복잡도(N) = 500,000 > 여기서 X의 위치 파악하면 터짐.
    # X 위치 파악하는걸 분리,
    for word in words:
        s, t = word
        S.append(s.upper())
        T.append(t.upper())
        
    S = ''.join(S)
    T = ''.join(T)
    
    # 시간복잡도(N) = 1,000,000 
    for i in range(len(S)):
        if S[i] == 'X':
            # answer += str(T[i])
            print(str(T[i]), end='')
    
    
    # return answer
        
solution(N, words)