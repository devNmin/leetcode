class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0
        elif x == 1 or x == 2 or x == 3:
            return 1
        else:
            half_x = x // 2
            for i in range(1,half_x+1):
                value = i * i
                if value < x:
                    pass
                elif value == x:
                    return i
                else:
                    return i - 1
        return i




        