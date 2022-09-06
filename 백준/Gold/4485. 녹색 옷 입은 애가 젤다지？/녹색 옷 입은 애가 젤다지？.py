import sys
from heapq import heappop,heappush

input = sys.stdin.readline
dr = [-1,1,0,0]
dc = [0,0,-1,1]

i = 0
while True:
    N = int(input())
    if N == 0: break
    def dijsktra(N):
        # N = int(input())
        graph = [list(map(int,input().split())) for row in range(N)]

        def graph_check(r,c):
            return 0<= r < N and 0<= c <N
        
        inf = int(1e18)
        dist = [[inf for col in range(N)] for row in range(N)]

        heap = []
        heappush(heap,(graph[0][0],0,0)) # (비용,행,열)
        dist[0][0] = graph[0][0]

        while heap:
            d, cur_r,cur_c = heappop(heap)

            if dist[cur_r][cur_c] != d: continue

            for k in range(4):
                nr = cur_r + dr[k]
                nc = cur_c + dc[k]
                if graph_check(nr,nc) and\
                    dist[nr][nc] == inf:
                    dist[nr][nc] = d + graph[nr][nc]
                    heappush(heap,(dist[nr][nc],nr,nc))

        return dist[N-1][N-1]
    i+=1
    print(f"Problem {i}: {dijsktra(N)}")