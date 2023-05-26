N = int(input())
M = N
cnt = 0
while True :
    if N%5 == 0 :
        cnt = N//5
        break
    else:
        M -= 3
        cnt += 1
        if M%5 == 0 :
            cnt += (M//5)
            break
        elif (M < 5) and M !=3 :
            cnt = -1
print(cnt)