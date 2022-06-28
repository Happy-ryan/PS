limit = int(input())
record = int(input())
if record > limit:
    over = record - limit
    if  1<= over and over <= 20 :
        fine = 100
    elif 21<= over and over <= 30 :
        fine = 270
    else : fine = 500
    anw= 'You are speeding and your fine is $%d.' %fine
    print(anw)
else : print('''Congratulations, you are within the speed limit!''')