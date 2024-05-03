# https://www.acmicpc.net/problem/25381
from collections import deque, defaultdict

s = input()


def solution(s: str):
    
    # idea
    # 1. A는 -> 뒤에 있는 B 를 바라본다.
    # 2. C는 <- 앞에 있는 B를 바라본다.
    # 3. 포인트는 A와 C 모두 B를 바라본다는 점.
    # 4. 시행1과 시행2는 교환법칙 성립(경험)
    # 5. 따라서 시행1 -> 시행2 진행
    # 6. A1..B1..A2.....B2... 뒤에 있는 A부터 삭제한다.
    # 7. A1랑 만날 수 있는 B의 후보는 2개 / A2랑 만날 수 있는 B의 후보 1개
    # 8. 만약 A1 - B2 >  BA / A2-B2, A1-B1 > 0
    # 9. 즉 뒤에 있는 A는 선택할 수 있는 B의 개수가 가장 적다. 그래서 최대한 먼저 지워주도록 한다.
    
    # 인덱스 에러
    # 리스트, 큐 등에서 인덱스 사용할 때 항상 반드시 존재하는지 존재성 if문에 반드시 기록

    cnt = 0
    
    B_queue = deque([])
    for idx, x in enumerate(s):
        if x == "B":
            B_queue.append(idx)

    def remove_A(s, target):
        nonlocal cnt

        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == target:
                if B_queue and B_queue[-1] > idx:
                    B_queue.pop()
                    cnt += 1


    def remove_B(s, target):
        nonlocal cnt

        # <- 방향을 보므로 C는 앞에 있을수록 기회가 적다
        # 따라서 C는 정방향으로 판단한다.
        for idx in range(len(s)):
            if s[idx] == target:
                if B_queue and B_queue[0] < idx:
                    # C와 가장 빠르게 만나는 B를 제거 
                    # 따라서 인덱스 앞에서부터 제거된다.
                    B_queue.popleft()
                    cnt += 1


    remove_A(s, "A")
    # print("제거", first)
    remove_B(s, "C")
    # print("최종", second)


    return cnt

print(solution(s))