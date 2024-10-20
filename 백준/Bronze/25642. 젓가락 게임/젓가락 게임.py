yt, yj = map(int, input().split())
# print(f"용태: {yt}, 유진: {yj}")
while True:
    # 용태 > 유진 공격
    yj += yt
    # print(f"용태: {yt}, 유진: {yj}")
    if yt >= 5:
        print('yj')
        break
    if yj >= 5:
        print('yt')
        break
    # 유진 > 용태 공격
    yt += yj
    # print(f"용태: {yt}, 유진: {yj}")
    if yt >= 5:
        print('yj')
        break
    if yj >= 5:
        print('yt')
        break