from collections import Counter


def solution(n, m, ranks):
    dic = Counter()
    
    for rank in ranks:
        for num in rank:
            dic[num] += 1
    
    rank_list = list(dic.items())
    rank_list.sort(key=lambda x : -x[1])
    
    first_rank = rank_list[0][1]
    second_rank = 0
    
    second = []
    # print(rank_list)
    for num, rn in rank_list:
        if rn != first_rank and second_rank == 0:
            second_rank = rn
        if second_rank == rn:
            second.append(num)
    
    second.sort()
    return second
    
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    ranks = [list(map(int, input().split())) for _ in range(n)]
    print(*solution(n, m, ranks))