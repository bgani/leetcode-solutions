class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
         # Two Binary searches approach O(logm + logn)

        # Binary searches #1 - Find Row
        ROWS, COLS = len(matrix), len(matrix[0])

        # top and bottom pointers
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1 # target might be in bottom subarrrays
            elif target < matrix[row][0]:
                bot = row - 1 # target might be in top subarrays
            else: 
                break # target might be in current row
        
        # if top and bot crossed each other, there is no target
        if not (top <= bot):
            return False
        
        # find current row by top and bot values from previous binary search on matrix rows
        row = (top + bot) // 2


        # Binary searches #1 - Find target from row that was found in Binary Search #1
        # left and right pointers
        l, r = 0, COLS 
        while l <= r:
            m = (l + r) // 2 # find mid
            if target > matrix[row][m]:
                l = m + 1 # eliminate left side, move left pointer to m + 1
            elif target < matrix[row][m]:
                r = m - 1 # eliminate right side, move right pointer to m - 1
            else: 
                return True # target is equal to mid
        return False # left and right crossed each other, target not found