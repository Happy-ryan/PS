# https://www.acmicpc.net/problem/1713
from collections import deque, defaultdict

n = int(input())
p = int(input())
nums = list(map(int, input().split()))

# 1. 학생들이 추천을 시작하기 전에는 모든 사진 틀이 비어 있다.
q = deque([])
# 추천횟수 관리, 시간관리
recommendations = {}
times = {}
# 2. 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
# 2-1. 비어있는 틀이 없는 경우 -> 가장 추천 수 작은 학생 삭제 -> 가장 오래된 사진 삭제
def find(recommendations, times):
    res = []
    for (num, re), time in zip(recommendations.items(), times.values()):
        res.append((num, re, time))
    res.sort(key=lambda x: (x[1], -x[2]))
    # 가장 추천 수가 작으면서 가장 오래된 후보의 숫자를 뽑을 것!
    return res[0][0]
        
for num in nums:
    if len(q) == n and num not in recommendations:
        remove_num = find(recommendations, times)
        q.remove(remove_num)
        recommendations.pop(remove_num)
        times.pop(remove_num)
        q.append(num)
        recommendations[num] = 1
        times[num] = 0
    else:
        if num not in q:
            q.append(num)
            recommendations[num] = 1
            times[num] = 0
        else:
            recommendations[num] += 1
            
    for num in times.keys():
        times[num] += 1
            
print(*sorted(q))