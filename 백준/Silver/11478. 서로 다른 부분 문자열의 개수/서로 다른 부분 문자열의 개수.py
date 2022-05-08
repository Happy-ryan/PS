S = input()
result=[]
for i in range(len(S)) :
    for j in range(i+1,len(S)+1) :
            ss = S[i:j]
            result.append(ss)
result = set(result)    
print(len(result))