class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Left (low) and Right (high) pointers
        L, R = 0, len(nums) - 1

        while L <= R:
        # find mid point
            mid = (L + R) // 2

            # if target is on right side move Left pointer to mid + 1
            if target > nums[mid]:
                L = mid + 1
            # if target is on left side move Right pinter to mid - 1
            elif target < nums[mid]: 
                R = mid - 1
            else: # if target not bigger or less than nums[mid] then mid is targets index
                return mid                
        return -1 # if Left pointer gets bigger than Right / Right gets smaller than Left we are out of bound and couldn't find target