from heapq import heappop, heappush

n = int(input())
lessons = [list(map(int, input().split())) for _ in range(n)]
# 기존 회의실 배정과 달리 공강 시간을 최대한 줄이기 위해서 시작이 빠른 것이 오도록 정렬
lessons.sort(key=lambda x: (x[0], x[1]))

heap = []
last_time = lessons[0][-1]
heappush(heap, last_time)

cnt = 1
for s, e in lessons[1:]:
    last_time = heappop(heap)
    if s < last_time:
        cnt += 1
        # s가 last_time보다 작다는 건 아직 강의 진행 중,,,종료가 안되었으므로 다시 넣기!
        heappush(heap, last_time)
    # 강의가 시작되면 반드시 끝나는 시간을 기록되어야함!
    heappush(heap, e)
print(cnt)        