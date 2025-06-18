n, k = map(int, input().split())

s_cnt = 0 # 가장 최근에 저장한 총알의 수
cnt = 0 # 현재 가지고 있는 총알의 수

for time in range(n):
    cmd = input()
    if cmd == 'load':
        if time == 0:
            print(0)
        else:
            cnt = s_cnt
            print(cnt)
    elif cmd == 'ammo':
        cnt += k
        print(cnt)
    elif cmd == 'shoot':
        cnt -= 1
        print(cnt)
    elif cmd == 'save':
        s_cnt = cnt
        print(s_cnt)