n, a, b = map(int, input().split())

def solution(n, a, b):
    A, B = 1, 1
    for _ in range(n):
        A += a
        B += b
        if B > A:
            A, B = B, A
        elif A == B:
            B -= 1
    return A, B

print(*solution(n, a, b))