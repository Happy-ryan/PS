def solution(A, B):
    # A > B > C
    # (A + B + C) / 3 = B
    return 2 * A - B

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(solution(A, B))