class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            temp = ""
            for i in range(1, len(s)):
                summ = (int(s[i]) + int(s[i - 1])) % 10
                temp += str(summ)
            s = temp
        if s[0] == s[1]:
            return True
        return False