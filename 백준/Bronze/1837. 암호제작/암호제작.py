p, k = map(int, input().split())

def solution(p, k):
    for i in range(2, k):
        if p % i == 0:
            return f"BAD {i}"
    return "GOOD"

print(solution(p, k))