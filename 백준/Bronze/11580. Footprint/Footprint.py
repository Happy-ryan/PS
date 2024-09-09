l = int(input())
cmds = list(input())

# 서 동 남 북
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 0, 0

result = set()
result.add((x, y))
for cmd in cmds:
    if cmd == 'S':
        x += dx[2]
        y += dy[2]
    elif cmd == 'N':
        x += dx[3]
        y += dy[3]
    elif cmd == 'W':
        x += dx[0]
        y += dy[0]
    else:
        x += dx[1]
        y += dy[1]
    
    # print(x, y)
    result.add((x, y))
    
# print(result)
print(len(result))