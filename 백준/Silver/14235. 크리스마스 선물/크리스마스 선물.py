from heapq import heappush, heappop

n = int(input())
presents = [list(map(int, input().split())) for _ in range(n)]


def solution(n, presents):
    heap = []
    answer = ""
    for row in presents:
        if row[0] == 0:
            if len(heap) == 0:
                answer += "-1\n"
            else:
                answer += f"{-heappop(heap)}\n"
        else:
            for present in row[1:]:
                heappush(heap, -present)
    return answer[:-1]


print(solution(n, presents))