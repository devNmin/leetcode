def check_k(s: str) -> bool:
    return s == s[::-1]

def num_to_base(num: int, base: int) -> str:
    result = ""
    while num > 0:
        result = str(num % base) + result
        num //= base
    return result or "0"

def generate_all_palindromes():
    length = 1
    while True:
        half_start = 10**((length - 1) // 2)
        half_end = 10**((length + 1) // 2)
        for half in range(half_start, half_end):
            s = str(half)
            if length % 2 == 0:
                yield int(s + s[::-1])
            else:
                yield int(s + s[-2::-1])
        length += 1

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        cnt = 0
        res_sum = 0

        for num in generate_all_palindromes():
            if check_k(num_to_base(num, k)):
                res_sum += num
                cnt += 1
                if cnt == n:
                    break

        return res_sum
