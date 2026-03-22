n, m = map(int, input().split())
j = int(input())
apples = [int(input()) for _ in range(j)]

s, e = 1, m
dist = 0

for apple in apples:
    if s <= apple <= e:
        continue
    # dist로 이동하는게 아니다
    # dist는 누적거리..
    if apple < s:
        move = s - apple
        dist += move
        s -= move
        e -= move
        
    elif apple > e:
        move = apple - e
        dist += move
        s += move
        e += move

print(dist)