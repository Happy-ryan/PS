# https://www.acmicpc.net/problem/27393
# 4 x 3 = 12가지 -> 브루트포스로 충분히 가능


def cal(cmd, x, y):
    if cmd == "+":
        x += y
    elif cmd == "-":
        x -= y
    elif cmd == "*":
        x *= y
    else:
        if x % y == 0:
            x //= y
        else:
            x = -int(1e8)
    return x
        
a, b, c = map(int, input().split())

cmds = ["+", "-", "*", "/"]

ans = int(1e8)
for i in range(4):
    k1 = cal(cmds[i], a, b)
    for j in range(4):
        k2 = cal(cmds[j], k1, c)
        if k2 >= 0:
            ans = min(ans, k2)
print(ans)       

