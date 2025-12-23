n = int(input())
map = [list(input()) for _ in range(n)]

def solution(n, map):
    
    def find_bomb():
        bombs = []
        for i in range(n):
            for j in range(n):
                if map[i][j] != '.':
                    bombs.append((i, j))
        return bombs
    
    bombs = find_bomb()
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n
    
    dir = [ (-1, -1), (-1, 0), (-1, 1),
            (1, -1), (1, 0), (1, 1),
            (0, 1), (0, -1)
            ]

    new_map = [[0 for _ in range(n)] for _ in range(n)]
    
    inf = -int(1e8)
    
    for bomb in bombs:
        cr, cc = bomb
        new_map[cr][cc] = inf
        for d in dir:
            nr = cr + d[0]
            nc = cc + d[1]
            if in_range(nr, nc):
                new_map[nr][nc] += int(map[cr][cc])
    

    for i in range(n):
        for j in range(n):
            x = new_map[i][j]
            if x < 0:
                print('*', end='')
            elif x < 10 :
                print(x, end ='')
            else:
                print('M', end='')
        print()

solution(n, map)