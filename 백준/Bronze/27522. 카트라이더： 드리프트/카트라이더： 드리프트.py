recodes = list(input() for _ in range(8))

ranking = []

for row in recodes:
    recode, team = row.split(' ')
    m, s, ss = recode.split(':')
    # 1s = 1000ss
    # 1m = 60s = 60 * 1000ss
    val = m * 60 * 1000 + s * 1000 + ss
    ranking.append((val, team))
    
ranking.sort(key=lambda x : x[0])

score = {
    1 : 10,
    2 : 8, 
    3 : 6,
    4 : 5,
    5 : 4,
    6 : 3,
    7 : 2,
    8 : 1
}
s_red, s_blue = 0, 0
for idx, info in enumerate(ranking):
    team = info[1]
    if team == 'B':
        s_blue += score[idx + 1]
    else:
        s_red += score[idx + 1]
        
if s_blue > s_red:
    print('Blue')
else:
    print('Red')