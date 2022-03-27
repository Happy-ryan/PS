import sys
T = int(input())
for _ in range(T) :
    H, W, N = map(int, sys.stdin.readline().split())
    cnt = 1 # 호수를 나타낸다
    while N > H :
        N = N -H # while문 빠져나오면 층수를 의미한다.
        cnt += 1
    print(f"{N*100+cnt}") 