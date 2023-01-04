change = 1000 - int(input())
money = [500, 100, 50, 10, 5, 1]
cnt = 0
while change != 0:
    if change >= 500:
        change -= 500
        cnt += 1
    else:
        if change >= 100:
            change -= 100
            cnt += 1
        else:
            if change >=50:
                change -= 50
                cnt += 1
            else:
                if change >= 10:
                    change -= 10
                    cnt += 1
                else:
                    if change >= 5:
                        change -= 5
                        cnt += 1
                    else:
                        change -= 1
                        cnt += 1

print(cnt)