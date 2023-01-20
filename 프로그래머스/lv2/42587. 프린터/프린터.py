from collections import deque

def solution(priorities, location):
    # location  = 내가 요청한 문서의 인덱스
    L = len(priorities)
    order = 0
    point = 0
    while True:
        if max(priorities) == priorities[point%L]:
            priorities[point%L] = 0
            order += 1
            # point % L : if문 통과 > 우선순위 제일 큰 놈의 인덱스 > 출력
            # location : 내가 요청 문서의 인덱스
            # == : 내가 요청한 것이 최고 우선순위를 가지므로 출력한다.
            if point%L == location:
                break
        point += 1   
    return order