class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack(start, path):
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(nums[i], path)
                path.pop()
                used[i] = False

        backtrack(0, path)
        return result