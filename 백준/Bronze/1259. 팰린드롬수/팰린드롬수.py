while True :
    n = int(input())
    a = len(str(n))
    result = "yes"
    if n== 0 :
        break
    else:
        if a%2 == 0 :
            for i in range(a//2) :
                if str(n)[i] == str(n)[a-1-i] :
                    result = "yes"
                else :
                    result = "no"
                    break
            print(result)
        else :
            for i in range(a//2) :
                if str(n)[i] == str(n)[a-1-i] :
                    result = "yes"
                else :
                    result = "no"
                    break
            print(result)
