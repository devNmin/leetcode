class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        value = 0
        power = 1

        # 뒤에서부터 k 이하인 범위까지 1 포함
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                count += 1  # 0은 무조건 포함
            else:
                if power <= k and value + power <= k:
                    value += power
                    count += 1
                # 이후 power가 너무 커지면 탈출 (안전하게 2^31 이상이면 stop)
            power *= 2
            if power > k:
                break

        # 앞쪽에 있는 0들은 그냥 다 추가로 포함 가능
        for j in range(i - 1, -1, -1):
            if s[j] == '0':
                count += 1

        return count
