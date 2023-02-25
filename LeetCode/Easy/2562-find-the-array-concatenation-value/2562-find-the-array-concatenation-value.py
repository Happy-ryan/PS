class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        if len(nums) % 2 == 0:
            for i in range(len(nums)//2):
                res += int(str(nums[i]) + str(nums[len(nums) - i - 1]))
        else:
            for i in range(int(len(nums)//2)):
                res += int(str(nums[i]) + str(nums[len(nums) - i - 1]))
            res += nums[int(len(nums)//2)]
        
        return res