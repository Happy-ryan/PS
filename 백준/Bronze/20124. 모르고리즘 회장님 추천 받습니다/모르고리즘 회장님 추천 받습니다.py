n = int(input())
A = [list(input().split()) for _ in range(n)]

def solution(n, A):
    A.sort(key=lambda x : (-int(x[1]), x[0]))
    return A[0][0]

print(solution(n, A))