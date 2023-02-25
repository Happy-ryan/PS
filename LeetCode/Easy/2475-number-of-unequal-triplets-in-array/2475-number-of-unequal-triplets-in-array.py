class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        from itertools import combinations
        ans = 0
        for x1, x2, x3 in combinations(nums, 3):
            if x1 != x2 and x2 != x3 and x1 != x3:
                ans += 1
        return ans