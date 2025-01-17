N = int(input())
A = list(map(int, input().split()))
M = int(input())
QS = [list(map(int, input().split())) for _ in range(M)]

from heapq import heappush, heappop

def solution(N, A, M, QS):
    A = [0] + A
    
    heap1 = []
    
    for idx, num in enumerate(A):
        if idx == 0:
            continue
        heappush(heap1, (num, idx))
    
    for q in QS:
        if q[0] == 1:
            # 배열 관리
            A[q[1]] = q[2]
            # 기존 값을 굳이 pop할 필요는 없음
            # 2명령어를 수행할 때 최신화할 예정
            heappush(heap1, (q[2], q[1]))
        else:
            while heap1:
                num, idx = heappop(heap1)
                # A[idx]와 num이 일치하지 않는다는 것
                # 최소로 뽑힌 num이 실제 최솟값이 아니라 예전 최솟값임을 의미한다.
                # 따라서 그 값은 pop한 상태에서 다시 push할 필요 없다.
                if A[idx] == num:
                    print(idx)
                    heappush(heap1, (num, idx))
                    break
                    
                
                
        # print(f"heap1: {heap1}")
        # print("=")
        
        
solution(N, A, M, QS)