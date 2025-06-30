class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}  # 숫자별 빈도수 저장용 딕셔너리

        # 1단계: 빈도수 직접 계산
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        max_len = 0

        # 2단계: num + 1 이 존재할 때만 계산
        for num in freq:
            if num + 1 in freq:
                max_len = max(max_len, freq[num] + freq[num + 1])

        return max_len
