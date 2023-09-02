from collections import Counter

t = int(input())

for _ in range(t):
    day = int(input())
    lottos = [list(map(int, input().split())) for _ in range(day)]
    flat_lotto = [row for lotto in lottos for row in lotto]
    dic = Counter(flat_lotto)
    
    num_cnt_list = list(dic.items())

    # 나온 횟수 x[1] 내림차순 1순위
    # 횟수 동일할 경우 x[0] 작은수 올림차순 2순위
    num_cnt_list.sort(key = lambda x : (-x[1], x[0]))
    key_list = [key for key, _ in num_cnt_list]

    #print(num_cnt_list)

    if 7 not in key_list:
        res = num_cnt_list[:6]
    else:
        idx = key_list.index(7)
        # 6번째 숫자의 나타난 횟수..6개의 숫자 중 가장 작거나 같다.
        min_cnt = num_cnt_list[5][1]
        if 6 <= idx and num_cnt_list[idx][1] == min_cnt:
            res = num_cnt_list[:5] + [num_cnt_list[idx]]
        else:
            res = num_cnt_list[:6]

    for i, _ in sorted(res):
        print(i, end = " ")
    print()
