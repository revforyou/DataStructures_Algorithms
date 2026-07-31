class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            ana_map[sorted_s].append(s)

        for value in ana_map.values():
            result.append(value)

        return result