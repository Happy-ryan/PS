from collections import deque

mod = 10000

def change_number(number: int, cmd: str):
    if cmd == 'D':
        number *= 2
        number %= mod
    elif cmd == 'S':
        number = (number + mod - 1) % mod
    elif cmd == 'L':
        d1 = number // 1000
        d2d3d4 = number % 1000
        number = d2d3d4 * 10 + d1
    elif cmd == 'R':
        d4 = number % 10
        d1d2d3 = number // 10
        number = d4 * 1000 + d1d2d3
        
    return number


def bfs(a, b):
    in_queue = [False for _ in range(mod)]
    inf = int(1e18)
    dist = [inf for _ in range(mod)]
    prev = [(-1, -1) for _ in range(mod)]
    
    def in_range(x):
        return 0 <= x < mod

    dq = deque([])
    dq.append(a)
    in_queue[a] = True
    dist[a] = 0
    prev[a] = (-1, -1)

    while dq:
        cx = dq.popleft()
        for cmd in ['D', 'S', 'L', 'R']:
            nx = change_number(cx, cmd)
            # print("cx: ", cx, "nx: ", nx)
            if in_range(nx) and not in_queue[nx]:
                dq.append(nx)
                in_queue[nx] = True
                dist[nx] = dist[cx] + 1
                # 위치 추적 & cmd 추척 > prev에 둘 다 기록하는 것!
                prev[nx] = (cx, cmd)
    s = ""
    while True:
        x, cmd = prev[b]
        if x == -1:
            break
        s += cmd
        b = x
    # s는..역추적의 결과이므로 반대로 !!
    # 역추적은 항상 주의하자
    return s[::-1]

n = int(input())
words = [list(map(int, input().split())) for _ in range(n)]
def solution(n, words):
    for word in words:
        a, b = word
        print(bfs(a, b))

solution(n, words)