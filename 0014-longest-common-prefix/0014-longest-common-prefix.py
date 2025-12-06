class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        template = strs[0]

        for i in range(len(template)):
            for s in strs[1:]:
                if i == len(s) or s[i] != template[i]:
                    return template[:i]

        return template
