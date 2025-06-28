class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append((s1[i], s2[i]))

        if len(diff) == 0:
            return True  # 완전히 같음
        if len(diff) != 2:
            return False  # 2개 초과면 swap으로 못 해결

        return diff[0] == diff[1][::-1]
