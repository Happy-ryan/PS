n, m = map(int, input().split())
times = list(map(int, input().split()))

def solution(n, m, times):
    # 정렬 불가
    
    # 블루레이의 크기..
    # 블루레이 크기 10 : (1 2 3 4) (5) (6) (7) (8) (9) 6개 F
    # 블루레이 크기 15 : (1 2 3 4 5) (6 7) (8) (9) 4개 F
    # 블루레이 크기 17 : (1 2 3 4 5) (6 7) (8 9) 3(m)개 T
    # 블루레이 크기 18 : (1 2 3 4 5) (6 7) (8 9) 3개 T
    # 블루레이 크기 1억 : (1 2 3 4 5 6 7 8 9) 1개 T
    # 블루레이 크기가 작아질수록 블루레이 숫자는 늘어남!!
    # 블루레이 크기가 클수록 블루레이 숫자는 감소함!! 단조증감 발견
    # 크기 :   1 ...   |17 18 ... 1억
    # 개수 :   9개      | 3 3      1개

    psum = [0] * (n + 1)
    for i in range(n):
        psum[i + 1] = psum[i] + times[i]
    def cal(size): # 블루레이 사이즈에 따른 블루레이의 수
        # 누적합..
        s, e = 0, 0
        cnt = 0
        while e <= n:
            # print(f"s: {s}, e: {e}, psum[e] - psum[s] :{psum[e] - psum[s]}")
            if psum[e] - psum[s] <= size:
                e += 1
            else:
                # print(f"*s: {s}, e: {e}, psum[e] - psum[s] :{psum[e] - psum[s]}*")
                cnt += 1
                s = e - 1
                e += 1
        # 마지막 상태 반영
        if psum[e - 1] - psum[s] <= size:
            cnt += 1
            
        # print(cnt)
        return cnt
    
    # print(psum)
    # cal(15)
    l, r = max(times), sum(times) + 1
    while l <= r:
        mid = (l + r) // 2
        if cal(mid) > m: # mid 블루레이 크기가 너무 작음..개수가 많아진 것 > 블루레이 크기 증가
            l = mid + 1
        else: # 블루레이 크기가 너무 커..개수가 적어졌어...크기 줄여야함
            r = mid - 1
    
    return l # 정답영역이 오른쪽이므로 l 출력

print(solution(n, m, times))