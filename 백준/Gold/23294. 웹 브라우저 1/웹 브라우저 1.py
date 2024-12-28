N, Q, C = map(int, input().split())
CAPS = list(map(int, input().split()))
QS = [list(input().split()) for _ in range(Q)]

from collections import deque 

def solution(N, Q, C, CAPS, QS):
    
    global total_capa, first
    
    CAPS = [0] + CAPS
    first = False
    
    back = deque([])
    front = deque([])
    access = deque([])
    
    def cal(arr):
        capa = 0
        for x in arr:
            capa += CAPS[x]
        return capa

    def cal_total_cal():
        return cal(back) + cal(access) + cal(front)
    
    total_capa = cal_total_cal()
        
    # 뒤로 가기 / 앞으로 가기는 최신거를 뒤에 넣고 stack 형식처럼 작동시키자!
    # 뒤록 가기 앞으로 가니는 최대 캐시의 변동은 없음!
    def BACK():
        if len(back) == 0:
            return
        ex_page = access.pop()
        front.append(ex_page) # 현재 페이지 -> 앞으로 가기 공간 맨 뒤에 넣기
        page = back.pop()
        access.append(page) # 뒤로 가기 공간 중 맨 뒤에 있는 최신 페이지 -> 현재 페이지 공간 이동
                            # 뒤로 가기 공간에서 맨 뒤에 있는 최신 페이지 삭제
        return 
    def FRONT():
        if len(front) == 0:
            return
        ex_page = access.pop()
        back.append(ex_page)
        page = front.pop()
        access.append(page)
        return
    def ACCESS(page):
        global total_capa, first
        # 1. 앞으로 가기 공간 초기화
        total_capa -= cal(front)
        front.clear() # 지역변수 / 전역변수 선언 주의
        # 2-1. 최초 접속
        if not first:
            access.append(page)
            total_capa += CAPS[page]
            first = True
            return
        # 2-2. 최초 접속 아님
        ex_page = access.pop()
        back.append(ex_page)
        access.append(page)
        total_capa += CAPS[page]
        if total_capa > C:
            while True:
                if total_capa <= C:
                    break
                ex_page = back.popleft()
                total_capa -= CAPS[ex_page]
        
    def COMPRESS():
        global total_capa, first
        new_back = deque([])
        # 압축이 되어야하지 순서는 유지해야함!
        while back:
            x = back.popleft()
            if not new_back:
                new_back.append(x)
            else:
                if new_back[-1] != x:
                    new_back.append(x)
                else:
                    total_capa -= CAPS[x]
        return new_back
    
    for idx, q in enumerate(QS):
        if q[0] == 'B':
            BACK()
        elif q[0] == 'F':
            FRONT()
        elif q[0] == 'A':
            ACCESS(int(q[1]))
        else:
            back = COMPRESS()
        
        # print(f"{idx + 1}번째 명령어: {q}")
        # print(f"뒤로가기공간: {back}")
        # print(f"현재 접속 : {access}")
        # print(f"앞으로가기공간: {front}")
        # print(f"total_capa: {total_capa}")
        # print("-")

    def print_area(arr):
        arr = list(arr)[::-1]
        if len(arr):
            print(*arr)
        else:
            print(-1)
    
    print_area(access)
    print_area(back)
    print_area(front)
        
solution(N, Q, C, CAPS, QS)