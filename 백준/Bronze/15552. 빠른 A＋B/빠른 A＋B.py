import sys
T = int(input())
for _ in range(T) :
    A, B=  map(int, sys.stdin.readline().split())
    ret = A + B
    print(ret)