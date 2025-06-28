from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # (index, value)로 묶고 → 값 기준 정렬 → 상위 k개 선택
        top_k = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)[:k]

        # 인덱스 기준 정렬 후 값만 추출
        return [val for idx, val in sorted(top_k, key=lambda x: x[0])]
