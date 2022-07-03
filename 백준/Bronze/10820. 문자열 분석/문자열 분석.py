# 입력의 종료값이 정해지지 않은 경우    
while True:
    try:
        s = input()
        def f(s):
            arr = 'abcdefghijklmnopqrstuvwxyz'
            brr = arr.upper()
            crr ='0123456789'
            cnt1=0
            cnt2=0
            cnt3=0
            cnt4=0
            for x in s:
                if x in arr:
                    cnt1+=1
                elif x in brr:
                    cnt2+=1
                elif x in crr:
                    cnt3 +=1
                else: cnt4 +=1
            return [cnt1,cnt2,cnt3,cnt4]
        print(*f(s))
    except EOFError:
        break