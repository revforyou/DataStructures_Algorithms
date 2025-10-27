class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        #O(nm)
        new = []
        for i in bank:
            if i.count("1") > 0:
                new.append(i)
        ans = 0
        for i in range(len(new) - 1):
            ans += new[i].count("1") * new[i + 1].count("1")
        return ans