
from collections import Counter
def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        day = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] == 0:
            days.append(day)
        else:
            day += 1
            days.append(day)
    # [7, 3, 2, 9] > 3과2는 7이 배포되기 전까지는 불가이므로 7까지 기다려야함
    # 즉 n번째 진행이 완료 즉시 배포되기 위해서는 1 ~ n - 1까지 완료된 날보다 더 뒤에 완료가 되어야 한다.
    # -----------------> max로 비교         
    answer = [days[0]]
    for i in range(1, len(days)):
        answer.append(max(answer[-1], days[i]))

    return list(Counter(answer).values())