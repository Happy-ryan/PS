t1 = list(input().split(':'))
t2 = list(input().split(':'))

def change(time):
    sum = 0
    sum += int(time[0]) * 3600
    sum += int(time[1]) * 60
    sum += int(time[2])
    return sum
        


if change(t1) < change(t2):
    print(change(t2) - change(t1))
else:
    print(change(t2) + 24 * 3600 - change(t1))