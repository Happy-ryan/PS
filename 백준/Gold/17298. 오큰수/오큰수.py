# 스택 접근
n = int(input())
numbers = list(map(int, input().split()))

def find_NGE(nums: list[int]):
    stack = []
    result = [-1] * len(nums)
    # 시간복잡도: O(N)
    for idx in range(len(nums)):
        # 스택이 있고 스택의 가장 위에 있는 것보다 새로운 num[idx]가 크면 기록!!
        # stack.pop(): 오큰수가 결정되므로 빼야함!
        # 시간복잡도: O(1)
        while stack and nums[stack[-1]] < nums[idx]:
            result[stack.pop()] = nums[idx]

        stack.append(idx)

    return result

result = find_NGE(numbers)

for res in result:
    print(res, end=" ")