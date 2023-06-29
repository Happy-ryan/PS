# https://www.acmicpc.net/problem/27239

n = int(input())

# 나머지
dic1 = {1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e",
        6: "f",
        7: "g",
        0: "h"   
        }

# 몫
dic2 = {0: "1",
        1: "2",
        2: "3",
        3: "4",
        4: "5",
        5: "6",
        6: "7",
        7: "8",
        }

p = n % 8
q = n // 8

if p == 0:
    print(dic1[p] + str(n//8))
else:
    print(dic1[p] + dic2[q])