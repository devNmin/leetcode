class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        for i in range(len(nums)-1):
            if (nums[i] % 2) + (nums[i+1] % 2) != 1:
                return False
        return True
            
               
        