from heapq import heappop, heappush

N = int(input())
nums = [int(input()) for _ in range(N)]

def solution(N, nums):
    
    heap = []
    answer = []
    # print("-")
    for idx, num in enumerate(nums):
        # print(f"heap: {heap}")
        if num == 0:
            if not heap:
                # print(0)
                answer.append(0)
            else:
                val = heappop(heap)
                answer.append(val[-1])
                # print(f"val: {val}")
        else:
            heappush(heap, (abs(num), num)) # 절대값으로 정렬 후 num 정렬
    # print("-")
    # print(answer)
    for a in answer:
        print(a)
        
solution(N, nums)