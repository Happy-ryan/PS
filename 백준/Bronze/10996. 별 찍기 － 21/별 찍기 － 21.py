N = int(input())

for i in range(N) :
    s1=""
    s2=""
    for j in range(N):
        if j%2==0 :
            s1 += ("*"+" ")
        else :
            s2 += (" "+"*")
    print(s1)
    print(s2)