s = input()
arr =[0]*26
for i in s :
    arr[ord(i)-97] += 1
print(*arr)