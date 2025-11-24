while True:
    try:
        d = int(input())
        # 시침 / 분침 모두 움직임 -> 시침 고정
        # 분침만 이동 30분 -> 180도 회전 / 1분 -> 6도 회전
        # 따라서 가능한 각도는 6의 배수

        if d % 6 == 0:
            print("Y")
        else:
            print("N")
    except:
        break