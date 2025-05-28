n = int(input())

des = [tuple(map(int, input().split())) for _ in range(n)]
des.sort(key=lambda x: -x[1])

print(*des[-1])