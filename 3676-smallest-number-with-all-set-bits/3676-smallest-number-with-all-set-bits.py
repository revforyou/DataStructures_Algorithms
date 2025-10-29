class Solution:
    def smallestNumber(self, n: int) -> int:
        bits = n.bit_length()
        x = (1 << bits) - 1
        
        if x < n:
            x = (1 << (bits + 1)) - 1
        
        return x