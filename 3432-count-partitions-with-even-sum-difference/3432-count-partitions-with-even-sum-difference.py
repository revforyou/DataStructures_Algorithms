class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        if total % 2 != 0:
            return 0
        
        # total is even → every split works
        return len(nums) - 1
