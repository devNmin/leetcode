class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        n = len(nums)
        pow2 = [1] * n
        
        # 미리 2^i 값 계산
        for i in range(1, n):
            pow2[i] = pow2[i - 1] * 2 % mod

        left, right = 0, n - 1
        result = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                result += pow2[right - left]
                result %= mod
                left += 1
            else:
                right -= 1

        return result
