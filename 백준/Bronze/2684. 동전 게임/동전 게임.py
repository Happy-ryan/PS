T = int(input())
for _ in range(T):
    arr = input()
    s,e=0,0
    cnt1,cnt2,cnt3,cnt4,cnt5,cnt6,cnt7,cnt8=0,0,0,0,0,0,0,0
    while s != len(arr)-2:
        e += 3
        row = arr[s:e]
        # print(row)
        if row =='TTT':
            cnt1 +=1
        elif row =='TTH':
            cnt2 +=1
        elif row == 'THT':
            cnt3 +=1
        elif row =='THH':
            cnt4 +=1
        elif row =='HTT':
            cnt5+=1
        elif row =='HTH':
            cnt6+=1
        elif row=='HHT':
            cnt7+=1
        else: cnt8 +=1     
        s += 1
        e = s
    print(cnt1,cnt2,cnt3,cnt4,cnt5,cnt6,cnt7,cnt8)