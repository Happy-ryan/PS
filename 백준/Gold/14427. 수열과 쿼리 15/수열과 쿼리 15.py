N = int(input())
A = list(map(int, input().split()))
M = int(input())
QS = [list(map(int, input().split())) for _ in range(M)]

from heapq import heappush, heappop

def solution(N, A, M, QS):
    A = [0] + A
    # 1번 명령어 - list의 경우 시간복잡도 문제 없음. 문제는 힙을 쓸 때 해당 인덱스를 가진 값을 어떻게 변경하냐는 이슈 발생
    # 내 생각에는 pop 시키면서 다른 곳에 저장해두다가 해당 인덱스 나오면 그 값 변경한 후 다른 힙에 넣으면 좋을 것 같음
    
    # 2번 명령어 - 가장 크기가 작은 값의 인덱스를 가져와야함 / 이 경우 풀 스캔하면 시간초과날 수밖에 없음
    # (숫자, 인덱스)를 묶어서 가지고 다녀서 heap를 사용해서 pop시키는 것이 합리적이라고 생각
    heap1 = []
    heap2 = []
    
    for idx, num in enumerate(A):
        if idx == 0:
            continue
        heappush(heap1, (num, idx))
    
    for q in QS:
        if q[0] == 1:
            A[q[1]] = q[2]
            heappush(heap1, (q[2], q[1]))
        else:
            while heap1:
                num, idx = heappop(heap1)
                if A[idx] == num:
                    print(idx)
                    heappush(heap1, (num, idx))
                    break
                    
                
                
        # print(f"heap1: {heap1}")
        # print("=")
        
        
solution(N, A, M, QS)