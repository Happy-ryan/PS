R, C = map(int, input().split())
races = [input() for _ in range(R)]

from collections import defaultdict

def solution(R, C, races):
    
    def getDistance(race):
        
        race = race[::-1]
        
        for i in range(1, C - 1):
            if race[i].isdigit():
                num = int(race[i])
                if 1<= num and num <= 9:
                    return (num, i)
        return (51, 51)

    candis = []
    
    for race in races:
        num, dis = getDistance(race)
        candis.append((num, dis))
        
    candis.sort(key=lambda x: (x[1])) # 거리순 정렬
    
    dic = defaultdict(list)
    
    # print(candis)
    
    for idx, candi in enumerate(candis):
        n, d = candi
        if d > 50:
            continue
        dic[d].append(n)
        
    ranking = [0] * 10
    cnt = 1
    for key, ranks in dic.items():
        for r in ranks:
            ranking[r] = cnt
        cnt += 1
        
    for r in ranking[1:]:
        print(r)


solution(R, C, races)