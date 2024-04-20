from heapq import heappop, heappush

# python에서는 기본적으로 최소 힙이므로 문제 해결을 위해 최대힙으로 변경
n, m = map(int, input().split())
presents = list(map(int, input().split()))
wishs = list(map(int, input().split()))


def solution(n, m, presents, wishs):

    heap = []

    # 선물이 많이 담겨있는 상자부터 가져가야함#
    # max heap
    for present in presents:
        heappush(heap, -present)

    for w in wishs:

        cur_present = -heappop(heap)

        # 선물 못나눠주면 망함!!
        if cur_present - w < 0:
            return 0
        
        # 다시 똑같은 상자 가져가도 되지만 가져간 만큼은 빼자
        heappush(heap, -(cur_present - w))

    return 1


print(solution(n, m, presents, wishs))