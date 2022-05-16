while True:
    s = input()
    if s==".":
        break
    arr=[]
    for x in s:
        if x=="(" or x==")" or x=="[" or x=="]":
            arr.append(x)
    ans = "yes"
    stack = []
    for x in arr:
        if x=="(" or x=="[":
            stack.append(x)
        else:
            if x ==")":
                if len(stack)==0:
                    ans="no"
                elif stack[-1]=="(":
                    stack.pop()
                else: 
                    ans = "no"
            else:
                if len(stack)==0:
                    ans="no"
                elif stack[-1]=="[":
                    stack.pop()
                else:
                    ans="no"
        
    if len(stack) !=0 :
        ans ="no"
    print(ans)