class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        for start in range(n):
            if nums[start]!=0:
                continue
            
            for direction in [1,-1]:
                arr=nums[:]
                curr=start
                dir=direction 

                while 0<= curr <n:
                    if arr[curr]==0:
                        curr+=dir
                    else:
                        arr[curr]-=1
                        dir*=-1
                        curr+=dir
                if all(x==0 for x in arr):
                    count+=1
            
        return count