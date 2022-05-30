month = int(input())
day = int(input())
if month == 1:
    print('Before')
elif month ==2:
    if day > 18:
        print('After')
    elif day ==18:
        print('Special')
    else: print('Before')
else: print('After')