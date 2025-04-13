n = int(input())
nums = list(map(int, input().split()))

from collections import Counter
        
def solution(n, nums):
    # 크기 1 - 5개
    # 크기 2 - 4개
    # 크기 3 - 3개
    # 크기 4 - 2개
    # 크기 5 - 1개
    
    # 크기k에 대한 판단 -> 슬라이딩 윈도우 feeling.. -> 시간복잡도(N^2) 해결이 안됨...
    # -> 다른 알고리즘 -> 투포인터..
    
    def slide():

        def cal(window):
            cnt = 0
            # 초기셋팅
            check = Counter(nums[:window])
            if len(check) == window:
                cnt += 1
            
            for i in range(n - window):
                # print("초기:", check)
                if len(check) == window:
                    cnt += 1
                check[nums[i]] -= 1
                if check[nums[i]] == 0:
                    check.pop(nums[i])
                # print("현재 위치 제거:", check)
                check[nums[i + window]] += 1
                # print("다음 위치 추가:", check)
                # print(f"cnt: {cnt}")            
            return cnt
        
        ans = 0
        # O(N^2)
        for w in range(1, n + 1):
            cnt = cal(w)
            ans += cnt
            
        return ans
    
    # 1 / 2 / 3 / 1 / 2      (5)
    # 1 2 / 2 3 / 3 1 / 1 2  (4)
    # 1 2 3 / 2 3 1 / 3 1 2  (3)
    
    
    #  한 쪽을 고정..! -> 투포인터 -> 한 쪽을 고정했을 때 중복없이 가장 긴 수열을 찾는 것!
    # 고정점 - 1 ...1
    # 고정점 - 2 ...2, 1 2
    # 고정점 - 3 ...3, 2 3, 1 2 3
    # 고정점 - 1 ...1, 3 1, 2 3 1
    # 고정점 - 2 ...2, 1 2, 3 1 2
    
    def two_pointer():
        dic = Counter()
        
        ans = 0
        
        r = -1
        for l in range(n):
            while r + 1 < n and  nums[r + 1] not in dic:
                dic[nums[r + 1]] += 1
                r += 1
            
            ans += r + 1 - l
            dic.pop(nums[l])
            
            
        return ans
            


    def two_pointer1(nums):
        n = len(nums)
        l = 0
        ans = 0
        seen = set()

        def valid(nums, l, r):
            return nums[r] not in seen

        def calc(nums, l, r):
            return r - l + 1

        for r in range(n):
            while not valid(nums, l, r):
                seen.remove(nums[l])
                l += 1

            seen.add(nums[r])
            ans += calc(nums, l, r)

        return ans
    
    return two_pointer()
        
print(solution(n, nums))