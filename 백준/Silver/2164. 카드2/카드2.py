import sys
n = int(sys.stdin.readline())
arr=list(range(1,n+1))
front = 0
while len(arr) != front+1:
    front += 1
    point = arr[front]
    arr.append(point)
    front +=1
print(arr[-1])