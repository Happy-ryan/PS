c1, d1 = map(int, input().split())
c2, d2 = map(int, input().split())
c3, d3 = map(int, input().split())
hp = int(input())

t = 0
while hp > 0:
    if t == 0:
        for d in [d1, d2, d3]:
            hp -= d
        if hp <= 0:
            break
    else:
        for c, d in [(c1, d1), (c2, d2), (c3, d3)]:
            if t % c == 0:
                hp -= d
        if hp <= 0:
            break
    t += 1
        
print(t)