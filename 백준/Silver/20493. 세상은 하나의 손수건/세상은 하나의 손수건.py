n, t = map(int, input().split())
arr = list(input().split() for _ in range(n))

def solution(n, t, arr):
    
    x, y, dir = 0, 0, 0
    pre_time = 0
    post_time = 0
    # 동(0) 남(1) 서(2) 북(3)
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    for (time, direction) in arr:
        time = int(time)
        post_time = time
        
        x += (post_time - pre_time) * 1 * dx[dir]
        y += (post_time - pre_time)* 1 * dy[dir]
        
        if direction == 'right':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
            
        t -= (post_time - pre_time)
        pre_time = post_time

    x += t * 1 * dx[dir]
    y += t * 1 * dy[dir]
    
    return x, y

print(*solution(n, t, arr))