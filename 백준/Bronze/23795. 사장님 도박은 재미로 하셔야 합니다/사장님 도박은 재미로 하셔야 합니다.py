playing = True
sum = 0
while playing:
    money = int(input())
    if money == -1:
        playing = False
    else:
        sum += money

print(sum)