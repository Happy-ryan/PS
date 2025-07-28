n = int(input())
arr = list(map(int, input().split()))

def solution(n, arr):
    # 정렬해도 아무 이슈 없음.
    arr.sort()
    
    # 이중 포문하면 시간초과 발생함..
    # 500,000 * 250,000
    mod = 1000000007
    # 시간초과 해결 : 이분탐색 / 투포인터 / 누적합 / 우선순위 큐 
    # 쌍을 결정하는 문제 - 하나 고정하고 생각...
    
    psum = [0] * (n + 1)
    for i in range(1, n + 1):
        psum[i] = psum[i - 1] + arr[i - 1]
    
    res = 0
    for r in range(n - 1, 0, -1):
        res += (arr[r] * psum[r]) % mod
        # print(arr[r], psum[r])
    
    # +한 값이 mod를 넘을 수 있음!! 주의
    return res % mod
    

print(solution(n, arr))