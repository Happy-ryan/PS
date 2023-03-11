class Solution:
    

    
    def passThePillow(self, n: int, time: int) -> int:
        # mod는 다시 돌아올 자기 자신으로 돌아올 때의 주기를 파악하는 것이다.
        # 1 2 3 4 3 2 //1 n = 4 mod = 4 + 2
        # 1 2 3 2// 1 n = 3 mod 3 + 1
        # mod = n + (n -2)
        nums = list(range(1, n + 1)) + list(range(n - 1, 0, -1))
        mod = len(nums) - 1
        return nums[time % mod]