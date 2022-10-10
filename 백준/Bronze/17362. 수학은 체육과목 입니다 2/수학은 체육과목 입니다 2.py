arr1 = [1,9,17,25] # 8 > 8로나눈 나머지 1
arr2 = [2,8,10,16,18] # 6 2 > 8로 나눈 나머지 2, 0
arr3 = [3,7,11,15] # 4 > 8로 나눈 나머지 3,7
arr4 = [4,6,12,14,20] # 2 6 > 8로 나눈 나머지 4,6
arr5 = [5,13,21,29] # 8 > 8로 나눈 나머지 5

n = int(input())
x = n%8
if x == 1:
    print(1)
elif x == 2 or x == 0:
    print(2)
elif x == 3 or x == 7:
    print(3)
elif x == 4 or x == 6:
    print(4)
else:
    print(5)