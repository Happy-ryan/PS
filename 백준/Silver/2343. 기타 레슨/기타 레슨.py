# https://www.acmicpc.net/problem/2343

# 이분탐색의 대상: 블루레이의 크기
# 3등분이 되게 하는 최소 블루레이의 크기
def binary_search(lectures):
    l, r = max(lectures), sum(lectures) + 1
    ans = l
    while l <= r:
        m = (l + r) // 2
        # 너무 많이 쪼개짐.
        # 블루레이 시간을 너무 작게 잡음.
        if get_count(m) >= M:
            l = m + 1
            ans = m
        else:
            r = m - 1
    return ans
    

def get_count(blueray: int):
    cnt = 0
    total = blueray
    for lecture in lectures:
        if lecture < total:
            total -= lecture
        else:
            cnt += 1
            total = blueray
            total -= lecture
    if total == 0:
        cnt += 1
    return cnt
    
N, M = map(int, input().split())
lectures = list(map(int, input().split()))
print(binary_search(lectures))