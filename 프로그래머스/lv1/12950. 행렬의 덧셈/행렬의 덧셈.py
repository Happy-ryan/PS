def solution(arr1, arr2):
    answer = [[0 for col in range(len(arr1[0]))] for row in range(len(arr1))]
    for r in range(len(arr1)):
        for c in range(len(arr1[0])):
            answer[r][c] = arr1[r][c] + arr2[r][c]
                
    return answer