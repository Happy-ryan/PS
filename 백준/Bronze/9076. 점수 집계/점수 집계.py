#https://www.acmicpc.net/problem/9076
def solution(scores: list):
    scores = sorted(scores)[1:len(scores) - 1]
    if abs(scores[-1] - scores[0]) >= 4:
        return "KIN"
    else:
        return sum(scores)


t = int(input())  # 테스트 케이스 개수를 입력받음
for _ in range(t):
    scores = list(map(int, input().split()))
    print(solution(scores))