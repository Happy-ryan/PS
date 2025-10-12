N = int(input().strip())
C = int(input().strip())
P = int(input().strip())

def solution(N, C, P):
    capacity = C * P
    return "yes" if N <= capacity else "no"

print(solution(N, C, P))