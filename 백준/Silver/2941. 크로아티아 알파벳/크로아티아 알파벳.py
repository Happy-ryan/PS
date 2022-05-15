S = input()
s = 0
cnt=0
while len(S) !=0 :
    if len(S)>=3:
        if S[0] == "d" and S[1] == "z" and S[2]=="=":
            S = S[3:]
            cnt+=1
            continue
    if len(S)>=2:
        if S[0] == "c" and S[1] == "=":
            S = S[2:]
            cnt+=1
            continue
        elif S[0] == "c" and S[1] == "-":
            S = S[2:]
            cnt+=1
            continue
        elif S[0] == "l" and S[1] == "j":
            S = S[2:]
            cnt+=1
            continue
        elif S[0] == "n" and S[1] == "j":
            S = S[2:]
            cnt+=1
            continue
        elif S[0] == "s" and S[1] == "=":
            S = S[2:]
            cnt+=1
            continue
        elif S[0] == "z" and S[1] == "=":
            S = S[2:]
            cnt+=1
            continue
        elif S[0] == "d" and S[1] == "-":
            S = S[2:]
            cnt+=1
            continue
    S = S[1:]
    cnt += 1
print(cnt)