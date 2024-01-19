from collections import defaultdict

n, c = map(int, input().split())
nums = list(map(int, input().split()))

# defaultdict을 사용할 때 기본값으로 리스트를 사용하고 싶다면 아래와 같이 정의
# [처음 나온 인덱스, 빈도]
fre = defaultdict(lambda: [0, 0])

for idx, num in enumerate(nums):
    if fre[num][0] == 0:
        fre[num][0] = idx + 1
    fre[num][1] += 1

arr = list(fre.items())
arr.sort(key=lambda x: (-x[1][1], x[1][0]))


for key, value in arr:
    print(f"{key} " * value[1], end="")