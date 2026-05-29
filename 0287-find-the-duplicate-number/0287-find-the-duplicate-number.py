class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #initialise 
        slow = nums[0]
        fast = nums[0]

        #detect the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        #find entrance of cycle 
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow


#DRY RUN example 2 nums = [3,1,3,4,2], Output = 3

#index : 0 1 2 3 4
#value : 3 1 3 4 2 (ARRAY Input)

# slow=3, fast=3
# slow=4, fast=2
# slow=2, fast=4
# slow=3, fast=3  (meet)

# slow=3 (reset), fast=3
# already equal → duplicate = 3

#Mapping 

# 0 -> nums[0] = 3    ,0 -> 3
# 1 -> nums[1] = 1    ,1 -> 1
# 2 -> nums[2] = 3    ,2 -> 3
# 3 -> nums[3] = 4    ,3 -> 4
# 4 -> nums[4] = 2    ,4 -> 2

#cycle is 0 -> 3 -> 4 -> 2 -> 3

# TIME COMPLEXITY : O(n) (work done is at most linear)

# SPACE COMPLEXITY : O(1), no data structure or extra space used, only pointers initialised

