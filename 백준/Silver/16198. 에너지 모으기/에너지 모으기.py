n = int(input())
arr = list(map(int, input().split()))

ans = 0
energy = 0
def dfs(level):
    global energy, arr, ans
    # level은 arr의 길이를 의미함.
    # Level이 2개 되면 더이상 에너지를 얻을 수 없음.
    if level == 2:
        ans = max(ans, energy)
        return
    # level은 배열의 길이를 의미. 첫번째와 미지막 구슬은 뽑을 수 없음.
    for idx in range(1, level - 1):
        # 복구하기 위해서 삭제하는 구슬 저장
        del_number = arr[idx]
        val = arr[idx - 1] * arr[idx + 1]
        # 에너지
        energy += val
        # 선택한 idx 슬라이싱으로 제거
        arr = arr[:idx] + arr[idx + 1:]
        dfs(level - 1)
        # 구슬 복구, 에너지 복구
        arr = arr[:idx] + [del_number] + arr[idx:]
        energy -= val

dfs(n)
print(ans)