# https://www.acmicpc.net/problem/1120

def same_length(A, B):
    cnt = 0
    for a, b in zip(A, B):
        if a != b:
            cnt += 1
    return cnt
# B의 맨 앞에서부터 움직여서 비교할 것
# topcoder - 8
# koder@@@ - 5
# @koder@@
# @@koder@
# @@@koder
# @는 내가 원하는대로 넣을 수 있다. 
# 그러므로 지금 있는 문자가 많이 겹쳐야한다.
# 시간복잡도: O(N^2)
def different_length(A, B):
    min_val = len(B)
    for i in range(0, len(B) - len(A) + 1):
        val = 0
        for j in range(i, i + len(A)):
            # A에는 j 자체를 넣는게 아니다. A는 0 ~ len(A) - 1이 범위이므로 조절해여함.
            if A[j - i] != B[j]:
                val += 1
        min_val = min(min_val, val)
    return min_val

A, B = input().split()

if A in B:
    print(0)
else:
    if len(A) == len(B):
        print(same_length(A, B))
    else:
        print(different_length(A, B))