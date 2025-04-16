h, w, n, m = map(int, input().split())

def solution(h, w, n, m):
    
    r_cnt, c_cnt = 0, 0
    r, c = 1, 1
    while True:
        if r > h:
            break
        r_cnt += 1
        r += (n + 1)

    while True:
        if c > w:
            break
        c_cnt += 1
        c += (m + 1)

    return r_cnt * c_cnt
        

print(solution(h, w, n, m))