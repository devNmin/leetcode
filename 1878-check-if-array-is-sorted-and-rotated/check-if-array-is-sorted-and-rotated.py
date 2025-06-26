class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0  # 정렬이 어긋나는 지점의 개수
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                if count > 1:
                    return False
                
        return True
