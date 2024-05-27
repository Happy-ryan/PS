arr = list(map(int, input().split()))

def solution(arr):
    if arr == sorted(arr):
        return 'Good'
    return 'Bad'

print(solution(arr))