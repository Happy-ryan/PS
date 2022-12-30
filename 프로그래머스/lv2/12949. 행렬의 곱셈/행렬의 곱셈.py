def solution(arr1, arr2):
    R1, C1 = len(arr1), len(arr1[0])
    R2, C2 = len(arr2), len(arr2[0])
    answer = [[0 for col in range(C2)] for row in range(R1)]
    for r1 in range(0, R1):
        for c2 in range(0, C2):
            for c1 in range(0, C1):
                answer[r1][c2] += arr1[r1][c1] * arr2[c1][c2]
    return answer