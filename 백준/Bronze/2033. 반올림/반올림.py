# https://www.acmicpc.net/problem/2033
# 시간복잡도: 정수N의 자리수 -> log2N

num_list = list(map(int, input()))
p = len(num_list) - 1
while p != 0:
    if num_list[p] >= 5:
        num_list[p] = 0
        num_list[p-1] = num_list[p-1] + 1
    else:
        num_list[p] = 0
    p -= 1
    
print(''.join(map(str, num_list)))