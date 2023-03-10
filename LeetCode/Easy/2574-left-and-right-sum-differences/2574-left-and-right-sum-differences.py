class Solution:
    
    
    def leftsum(nums: List[int]) -> List[int]:
        left = []
        for i in reversed(range(len(nums))):
            sum_val = sum(nums[:i])
            left.append(sum_val)
        return left[::-1]
            
        
    def rightsum(nums: List[int]) -> List[int]:
        right = []
        for i in range(len(nums)):
            sum_val = sum(nums[i+1:])
            right.append(sum_val)
        return right
        
        
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ans = []
        l = Solution.leftsum(nums)
        r = Solution.rightsum(nums)
        for i in range(len(nums)):
            ans.append(abs(l[i] - r[i]))
        
        return ans
    
# print(Solution.leftsum([10, 4, 8, 3]))
# print(Solution.rightsum([10, 4, 8, 3]))

