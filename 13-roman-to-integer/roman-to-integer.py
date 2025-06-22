mapping_values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
matching_patterns = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in matching_patterns:
                sum += matching_patterns[s[i:i+2]]
                i += 2
            else:
                sum += mapping_values[s[i]]
                i += 1
        return sum