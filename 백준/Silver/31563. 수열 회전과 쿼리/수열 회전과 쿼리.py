from collections import deque

n, q = map(int, input().split())
As = list(map(int, input().split()))
qs = deque([list(map(int, input().split())) for _ in range(q)])

def solution(n, q, As, qs):
    
    As = As + As
    
    psum = [0] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        psum[i] = psum[i - 1] + As[i - 1]
    
    def hap(a, b):
        return psum[b] - psum[a - 1]
        # print(psum)
    
    # qs 200,000
    # k 200,000 <- 직접 돌리다보면 시간초과가 날 수 있음.
    # 따라서 for문으로 직접 돌리지 않는 것이 필요함.
    # 슬라이싱, sum 모두 시간복잡도 O(n)
    # 슬라이싱안해도 돌리는걸 가정하는 순간 k만큼 필요함...그러면 무조건 아웃될 수밖에 없음.
    base = 0
    for q in qs:
        if q[0] == 1:
            base = (base + n - (q[1] % n)) % n # 음수가 될 때 보정
        elif q[0] == 2:
            base += q[1]
            base %= n
        else:
            # print(sum(As[q[1] - 1: q[2]]))
            # print("base: ", base, "a:", q[1] + base, "b", q[2] + base)
            print(hap(q[1] + base, q[2] + base))
        
        # print(f"명령어:{q[0]}, As: {As}")
            

solution(n, q, As, qs)