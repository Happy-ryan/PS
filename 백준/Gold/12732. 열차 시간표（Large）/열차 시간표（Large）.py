n = int(input())

from heapq import heappush, heappop

def solution(tc, T, NA, NB, trains):
    
    plan = []
    
    def cal_second(time):
        return int(time.split(":")[0]) * 3600 + int(time.split(":")[1]) * 60
    
        
    for idx in range(NA + NB):
        s, e = trains[idx]
        s = cal_second(s)
        e = cal_second(e)
        heappush(plan, (s, e, idx))

    cnt_a, cnt_b = 0, 0
    A, B = [], []
    while plan:
        s, e, idx = heappop(plan)
        if idx < NA:
            if not A:
                cnt_a += 1
            else:
                s_  = heappop(A)
                # A에 준비된 차량 존재!
                if s >= s_:
                    # print(f"idx: {idx}, 출발 차량 시각: {s}, 준비된 차량 시각:{s_}")
                    pass
                else:
                # A에 준비된 차량 없음!
                # 다시 넣고 / B로 새 열차 이동
                    cnt_a += 1
                    heappush(A, s_)
            # 무조건 차는 보내야해
            heappush(B, e + T * 60)
        else:
            if not B:
                cnt_b += 1
            else:
                s_  = heappop(B)
                # B에 준비된 차량 존재!
                if s >= s_:
                    # print(f"idx: {idx}, 출발 차량 시각: {s}, 준비된 차량 시각:{s_}")
                    pass
                # B에 준비된 차량 없음!
                # 다시 넣고 / A로 새 열차 이동
                else:
                    cnt_b += 1
                    heappush(B, s_)
            # 무조건 차는 보내야해
            heappush(A, e + T * 60)
            
        # print(f"s: {s}, e: {e}, idx: {idx}, A: {A}, B: {B}, cnt_a: {cnt_a}, cnt_b: {cnt_b}")

    
    return f"Case #{tc + 1}: {cnt_a} {cnt_b}"

for i in range(n):
    T = int(input())
    NA, NB = map(int, input().split())
    trains = [list(input().split()) for _ in range(NA + NB)]
    print(solution(i, T, NA, NB, trains))
