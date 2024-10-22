n = int(input())

for _ in range(n):
    m = int(input())
    missons = [list(map(int, input().split())) for _ in range(m)]
    k, d, a = map(int, input().split())
    sum_val = 0
    for mission in missons:
        val = k * mission[0] - d * mission[1] + a * mission[2]
        if val >= 0:
            sum_val += val
            
    print(sum_val)