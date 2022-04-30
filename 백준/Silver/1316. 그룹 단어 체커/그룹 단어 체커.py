T = int(input())
cnt = 0
for _ in range(T) :
    s = input()
    # compress aaa > a로 압축하기
    ss = [s[0]]
    for i in range(1,len(s)) :
        if s[i] == ss[-1] :
            pass
        else :
            ss.append(s[i])
    arr =[]
    for x in set(ss): # ss안에 압축된 것들이 있고 중복되는 문자 존재하는지 파악하는 코드
        ret = ss.count(x)
        arr.append(ret)
    #print(arr)
    if sum(arr) == len(arr) :
        cnt += 1
print(cnt) 
    