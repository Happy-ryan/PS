t = int(input())

def solution(c, v):
    return f"You get {c // v} piece(s) and your dad gets {c % v} piece(s)."


for _ in range(t):
    c, v = map(int, input().split())
    print(solution(c, v))