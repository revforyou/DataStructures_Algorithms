class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x>=0 else -1
        x = abs(x)
        rn = 0
        while x: 
            rn *= 10 
            rn += (x%10)
            if rn>(1<<31):
                return 0 
            x //= 10

        if (sign==1 and rn==(1<<31)): 
            return 0 
        return sign * rn