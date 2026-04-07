dic = {
    'Wide Receiver': (4.5, 150, 200),
    'Lineman': (6.0, 300, 500),
    'Quarterback': (5.0, 200, 300)
}

while True:
    sp, wide, weight = list(map(float, input().split()))
    anwser = []
    if sp == 0 and wide == 0 and weight == 0:
        break
    for key, value in dic.items():
        sp_, wide_, weight_ = value
        if sp <= sp_ and wide >= wide_ and weight >= weight_:
            anwser.append(key)
    if not anwser:
        print('No positions')
    else:
        print(*anwser)