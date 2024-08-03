def solution(n, feeds):
    day = 0
    while True:
        if sum(feeds) > n:
            return day + 1
        
        demand_feeds = [0] * 6
        for idx, feed in enumerate(feeds):
            demand_feeds[idx] = feed + feeds[(idx + 1) % 6] + feeds[(idx + 5) % 6] + feeds[(idx + 3) % 6]
        feeds = demand_feeds
        day += 1
        
        
t = int(input())
for _ in range(t):
    n = int(input())
    feeds = list(map(int, input().split()))
    print(solution(n, feeds))