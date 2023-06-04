# https://www.acmicpc.net/problem/2166
from pprint import pprint
n = int(input())
xy_list = [list(map(int, input().split())) for row in range(n)]
xy_list.append(xy_list[0])

sum_val1 = 0
sum_val2 = 0
for row in range(n):
    sum_val1 += xy_list[row][0] * xy_list[row + 1][1]
    sum_val2 += xy_list[row][1] * xy_list[row + 1][0]
    
print(f"{(0.5) *abs(sum_val1 - sum_val2):.1f}")