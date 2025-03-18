n = int(input())
A = []
B = []
for i in range(2 * n):
    if i % 2 == 0:
        A.append(list(map(int, input().split())))
    else:
        B.append(list(map(int, input().split())))

from collections import Counter

def solution(arr, brr):
    arr = Counter(arr[1:])
    brr = Counter(brr[1:])

    for i in range(1, 5):
        if i not in arr:
            arr[i] = 0
        if i not in brr:
            brr[i] = 0
            
    if arr[4] > brr[4]:
        return 'A'
    elif arr[4] < brr[4]:
        return 'B'
    else:
        if arr[3] > brr[3]:
            return 'A'
        elif arr[3] < brr[3]:
            return 'B'
        else:
            if arr[2] > brr[2]:
                return 'A'
            elif arr[2] < brr[2]:
                return 'B'
            else:
                if arr[1] > brr[1]:
                    return 'A'
                elif arr[1] < brr[1]:
                    return 'B'
                else:
                    return 'D'

for arr1, brr1 in zip(A, B):
    print(solution(arr1, brr1))