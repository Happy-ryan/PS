n, m = map(int, input().split())
arr = list(map(int,input().split()))

def solution(n, m, arr):
    # 정렬해도 무관
    arr.sort()
    inf = int(1e18)
    
    def cutting(h):
        cnt = 0
        for i in arr:
            if i >= h:
                cnt += (i - h)
        return cnt
    
    # 높이의 최대값
    # h 15 7개
    # 왼쪽 True 
    # h가 x 변수 / cutting 개수 y
    def binary_search(target):
        l, r = 0, inf
        ans = inf
        while l <= r:
            m = (l + r) // 2
            # 7의 왼쪽이 정답! > cutting시 target보다 큰값 중 가장 작은값의 최대값 구하기
            if cutting(m) >= target:
                l = m + 1
                ans = m
            else:
                r = m - 1
                
        return ans
    
    return binary_search(m)

print(solution(n, m, arr))