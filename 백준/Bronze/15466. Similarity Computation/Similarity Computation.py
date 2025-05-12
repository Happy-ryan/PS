t = int(input())

def solution(m, n, A, B):
    p = len(A & B)
    q = len(A | B)
    
    if p > 0.5 * q:
        return 1
    return 0

for _ in range(t):
    m, n = map(int, input().split())
    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))
    print(solution(m, n, A, B))