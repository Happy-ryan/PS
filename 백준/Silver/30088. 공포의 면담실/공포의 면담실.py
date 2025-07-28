n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def solution(n, arr):
    # 부서 소속원이 모두 면담 완료 = 부서원 모두 퇴사 가능
    # 부서의 퇴근 시간이 서로 영향을 미침..
    
    # 가설1. 면담 시간이 작은 순서로 정렬
    times = []
    for idx, row in enumerate(arr):
        times.append(sum(row[1:]))
        
    times.sort()
    
    psum = [0] * (n + 1)
    for i in range(1, n + 1):
        psum[i] = psum[i - 1] + times[i - 1]
    
    return sum(psum)

print(solution(n, arr))