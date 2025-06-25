class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                cnt +=1
            else:
                nums[i] = 101
        nums.sort()
        return cnt
