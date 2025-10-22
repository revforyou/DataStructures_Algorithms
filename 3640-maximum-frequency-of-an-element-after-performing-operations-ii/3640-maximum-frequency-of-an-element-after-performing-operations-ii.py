from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        C = Counter(nums)
        n = len(nums)
        ans = 0
        s, e = 0, 0
        nums.sort()
        for i in range(n):
            while s < n and nums[s]+k<nums[i]:
                s += 1
            while e < n and nums[e]-k<=nums[i]:
                e += 1
            ops = min(numOperations, e-s-C[nums[i]])
            ans = max(ans, C[nums[i]] + ops)
        
        s = 0
        for i in range(n):
            while s < n and nums[s]+k<nums[i]-k:
                s += 1
            ops = min(numOperations, i-s+1)
            ans = max(ans, ops)
        return ans