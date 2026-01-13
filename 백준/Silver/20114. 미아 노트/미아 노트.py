def solution(N, H, W, info):
    
    word = ['?' for _ in range(N)]
    
    for r in range(H):
        for c in range(W):
            for x in range(c * N, c * N + N):
                if info[r][x] != '?':
                    word[x // W] = info[r][x]
    

    return ''.join(word)

N, H, W = map(int, input().split())
info = [list(input()) for _ in range(H)]
print(solution(N, H, W, info))