n = int(input())
arr = [list(input().split()) for _ in range(n)]


def solution(n, arr):
    answer = ""
    max_level = 5
    for p, level in arr:
        level = int(level)
        if level <= max_level:
            max_level = level
            answer = p

    return answer


print(solution(n, arr))