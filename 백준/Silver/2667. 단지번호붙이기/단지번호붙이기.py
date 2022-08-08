n = int(input())
apt = ['#'*(n+2)]+['#'+input()+'#' for row in range(n)]+\
        ['#'*(n+2)]
# print(apt)
# print(apt[1])
# print(apt[1][1])
in_queue = [[False for col in range(n+1)] for row in range(n+1)]
cnt = []

# 이동방향
dr =[-1,1,0,0]
dc =[0,0,-1,1]
# apt 2차원 배열 안에서만 움직이도록 체크
def apt_check(r,c):
    return 1<= r <= n and 1<= c <= n

from collections import deque

for i in range(1,n+1):
    for j in range(1,n+1):
        if in_queue[i][j] == True:
            pass
        elif in_queue[i][j] == False and apt[i][j] == '0':
            pass
        else:
            q = deque([(i,j)]) 
            in_queue[i][j] = True # 방문 체크
            result = 1
            while q:
                r,c = q.popleft()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if apt_check(nr,nc) and\
                        not in_queue[nr][nc] and\
                            apt[nr][nc] =='1':
                            q.append((nr,nc))
                            in_queue[nr][nc] = True
                            result +=1
            cnt.append(result)
print(len(cnt))
for x in sorted(cnt):
    print(x)