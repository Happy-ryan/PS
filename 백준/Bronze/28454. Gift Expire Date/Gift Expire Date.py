y, m, d = map(int, input().split('-'))
n = int(input())
arr = [list(map(int, input().split('-'))) for _ in range(n)]

def solution(y, m, d, arr):
    cnt = 0
    for ny, nm, nd in arr:
        if y < ny:
            cnt += 1
        elif y == ny:
            if m < nm:
                cnt += 1
            elif m == nm:
                if d <= nd:
                    cnt += 1
    return cnt

print(solution(y, m, d, arr))