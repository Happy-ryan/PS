T = int(input())

for _ in range(T):
    input()
    N, M = map(int, input().split())
    p1 = list(input().split())
    p2 = list(input().split())
    answer = set()
    for p in p1:
        answer.add(p)
    for p in p2:
        answer.add(p)
    print(len(answer))