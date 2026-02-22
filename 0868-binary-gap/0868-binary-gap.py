class Solution:
    def binaryGap(self, v: int) -> int:
        return max(map(len,findall(r'10*(?=1)',bin(v))),default=0)