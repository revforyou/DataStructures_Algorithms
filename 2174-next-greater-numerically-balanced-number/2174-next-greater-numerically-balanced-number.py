class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(num):
            count = Counter(str(num))
            for d, freq in count.items():
                if int(d) != freq:
                    return False
            return True
        
        curr = n + 1
        while True:
            if is_balanced(curr):
                return curr
            curr += 1

            