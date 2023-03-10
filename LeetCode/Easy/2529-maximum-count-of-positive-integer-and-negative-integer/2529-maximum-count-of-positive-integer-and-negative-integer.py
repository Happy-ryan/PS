class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative_num = 0
        positive_num = 0
        for x in nums:
            if x > 0:
                positive_num += 1
            elif x < 0:
                negative_num += 1
            else:
                continue
        
        return max(negative_num, positive_num)
        