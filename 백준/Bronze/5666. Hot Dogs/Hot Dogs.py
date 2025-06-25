def solution(H, P):
    return f"{round(H / P, 2):.2f}"

while True:
    try:
        H, P = map(int, input().split())
        print(solution(H, P))
    except:
        break