import sys
N = int(input())
result = [0 for _ in range(10004)]
input = sys.stdin.readline
for _ in range(N) :
    n = int(input())
    result[n] += 1
for x in range(10004) :
    if result[x] != 0 :
        for y in range(result[x]) :
            sys.stdout.write(str(x)+"\n")