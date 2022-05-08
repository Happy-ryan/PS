import sys
N, M = map(int, sys.stdin.readline().split())
S = set([input() for _ in range(N)]) # list함수를 set으로 하는 이유 : (N) > (logN) 시간단축
check_str = list(input() for _ in range(M))
cnt = 0
for i in check_str :
    if i in S :
        cnt += 1
print(cnt)
