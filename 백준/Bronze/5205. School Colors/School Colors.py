K = int(input())

for t in range(1, K + 1):
    n = int(input())
    colors = [list(map(int, input().split())) for _ in range(n)]
    
    max_dist = -1
    result = []
    
    for i in range(n):
        for j in range(i + 1, n):
            r1, g1, b1 = colors[i]
            r2, g2, b2 = colors[j]
            
            dist = (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2
            
            if dist > max_dist:
                max_dist = dist
                result = [(i + 1, j + 1)]
            elif dist == max_dist:
                result.append((i + 1, j + 1))
    
    print(f"Data Set {t}:")
    for i, j in result:
        print(i, j)