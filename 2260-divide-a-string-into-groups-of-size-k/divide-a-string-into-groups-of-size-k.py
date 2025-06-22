class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        len_s = len(s)
        if len_s % k == 0:
            for i in range(0,len_s,k):
                res.append(s[i:i+k])
        else:
            for i in range(0,len_s,k):
                if i+k<=len_s:
                    res.append(s[i:i+k])
                else:
                    res.append(s[i:i+k]+ fill * (k-(len_s % k)))
        return res    
        