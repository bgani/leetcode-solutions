class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize the left and right boundaries
        l = 1 # min possible speed
        r = max(piles)
        res = r # initially res = r because we know that it's the max pile is a solution that could possibly be

        while l <= r:
            # compute the speed, k basically is a mid in binary search
            k = (l + r) // 2

            hours_spent = 0

            # Iterate over the piles and calc hours_spent.
            # we increase the hours_spent by ceil(pile / middle)
            for pile in piles:
                hours_spent += math.ceil(pile / k)

            # Check if middle is a workable speed, and cut the search space by half
            if hours_spent <= h:
                res = min(res, k) # take the min between res and k
                # now we look for even smaller k, eliminate right portion, search in left portion on next iteration
                r = k - 1 
            else:
                l = k + 1 # rate was too small, eliminate the left portion, search in right portion on next iteration
            
            # once the left and right switch sides we finished binary search
            # we return result because it's equal to min possible speed
        return res