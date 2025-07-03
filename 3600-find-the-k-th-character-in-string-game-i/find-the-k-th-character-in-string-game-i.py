class Solution:
    def kthCharacter(self, k: int) -> str:
        # 'a'에서 시작, popcount(k - 1)만큼 이동
        return chr(ord('a') + bin(k - 1).count('1'))
