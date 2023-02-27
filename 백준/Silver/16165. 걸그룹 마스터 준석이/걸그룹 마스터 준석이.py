from collections import defaultdict
n, m = map(int, input().split())
dic = defaultdict()
for _ in range(n):
    team_name = input()
    team_num = int(input())
    team_member = [input() for _ in range(team_num)]
    dic[team_name] = team_member
for _ in range(m):
    name = input()
    num = int(input())
    if num == 0:
        for x in sorted(dic[name]):
            print(x)
        
    else:
        for key, value in dic.items():
            if name in value:
                print(key)