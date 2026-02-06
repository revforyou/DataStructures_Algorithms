class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        i = 0
        for j in range(len(nums)):
            while nums[j] > nums[i] * k:
                i += 1
            count = max(count, j - i + 1)
        return len(nums) - count
        