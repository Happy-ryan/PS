S = input()
result = []
for i in range(len(S)):
   SS = S[i:]
   result.append(SS)
result = sorted(result)
for x in result :
    print(x)