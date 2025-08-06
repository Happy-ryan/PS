n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def solution(n, A, B):
    
    
    def binary(target):
        l, r = 0, n - 1
        while l <= r :
            m = (l + r) // 2
            # 정답영역
            if target < B[m]:
                r = m - 1
            else:
                l = m + 1
        return r
    
    for idx, a in enumerate(A):
        print(binary(a) - idx, end = ' ')
        
solution(n, A, B)