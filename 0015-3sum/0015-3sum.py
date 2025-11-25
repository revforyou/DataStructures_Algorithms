class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, n-1

            while l < r:
                threesum = nums[l] + nums[r] + nums[i]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    # Step 3: Found a triplet
                    res.append([nums[i], nums[l], nums[r]])
                    # Step 4: Skip duplicate elements for the second and third element
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1 
                    l += 1
                    r -= 1

        return res




