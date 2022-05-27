arr = [ input().split() for _ in range(9)]
arr = [[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h),int(i)] for a,b,c,d,e,f,g,h,i, in arr]
max_arr=[]
for i in range(9):
    max_num = max(arr[i])
    max_arr.append(max_num)
result = max(max_arr)
for i in range(9):
    if result in arr[i]:
        idx = arr[i].index(result)
        print(result)
        print(i+1,idx+1)
        break