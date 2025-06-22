class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res_dict = {

        }
        for num in nums:
            if num not in res_dict:
                res_dict[num] = 1
            else:
                res_dict[num] = 0
        result = 0
        for res_dict_key, res_dict_value in res_dict.items():
            if res_dict_value == 1:
                return res_dict_key

        