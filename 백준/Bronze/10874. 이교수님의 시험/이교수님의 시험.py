n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]

def solution(scores):
    member = []
    for idx, score in enumerate(scores):
        cnt = 0
        for number, s in enumerate(score):
            if (((number + 1) - 1) % 5) + 1 == s:
                cnt += 1
        if cnt == 10:
            member.append(idx + 1)

    for m in member:
        print(m)
        
solution(scores)