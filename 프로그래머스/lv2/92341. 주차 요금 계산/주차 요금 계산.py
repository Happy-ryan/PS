from collections import Counter
import math

def timeMin(time): # 시 : 분 > 분으로 변경하는 함수
    # time HH:MM
    time = time.split(":") 
    return int(time[0]) * 60 + int(time[1]) 

# Counter({'0148': 670, '0000': 334, '5961': 146})
def totalMoney(fees, numDict):
    res = []
    for key, value in numDict.items():
        if value > fees[0]:
            total = fees[1] + math.ceil((value - fees[0]) / fees[2]) * fees[3]
        else:
            total = fees[1]
        res.append((key, total))
    res.sort()
    return res

def solution(fees, records):
    answer = []
    res = []
    dic = {}
    for record in records:
        time, num, cmd = record.split()
        if cmd == 'IN':
            dic[num] = 0
            dic[num] -= timeMin(time) # IN일 때가 시간 계산의 기준값 (minus)
        else: # cmd가 out일 때
            dic[num] += timeMin(time) # plus
            res.append((num, dic[num]))
            dic.pop(num) # 출자 기록 없는 차를 찾기 위해서 출자한 차는 key에서 배제
    if len(dic.keys()) >= 1: # 출차 기록이 없다 > 23 * 60 + 59에 출차 간주
        for k in dic.keys(): # 출차 기록 없는 차에 대해서..
            res.append((k, dic[k])) # OUT이 없어서 res에 기록되지 않았음
            res.append((k, 23 * 60 + 59))
            
    # 차량넘버에 따른 총 시간 계산
    numDict = Counter()
    for row in res:
        numDict[row[0]] += row[1]
    
    res = totalMoney(fees, numDict)
    answer = [x[1] for x in res]
    return answer