class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Assuming array contains only 0, 1, 2
        counts = [0, 0, 0]

        # Count the quantity of each val in array
        for n in nums:
            counts[n] += 1
        
        # Fill each bucket in the original array
        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1