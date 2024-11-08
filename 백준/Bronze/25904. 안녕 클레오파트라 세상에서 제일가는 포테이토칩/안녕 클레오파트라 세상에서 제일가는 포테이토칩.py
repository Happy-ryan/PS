N, X = map(int, input().split())
limits = list(map(int, input().split()))

def solution(N, X, limits):
    idx = 0
    while True:
        if limits[idx] >= X:
            # print(f"person: {idx + 1}, voice: {X}")
            idx = (idx + 1) % N
            X += 1
        else:
            return idx + 1
    
print(solution(N, X, limits))