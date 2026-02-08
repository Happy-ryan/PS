while True:
    bal, act, val = input().split()
    
    bal = int(bal)
    val = int(val)

    if bal == 0 and act == 'W' and val == 0:
        break

    if act == 'D':
        print(bal + val)
    else:  
        if bal - val < -200:
            print("Not allowed")
        else:
            print(bal - val)
