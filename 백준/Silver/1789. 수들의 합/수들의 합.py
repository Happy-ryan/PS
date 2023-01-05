N = int(input())

def greedy(N):
    cnt = 0
    if N == 1:
        return 1
    else:
        for x in range(1, N + 1):
            N -= x
            if N >= 0:
                cnt += 1
            else:
                return cnt

print(greedy(N))