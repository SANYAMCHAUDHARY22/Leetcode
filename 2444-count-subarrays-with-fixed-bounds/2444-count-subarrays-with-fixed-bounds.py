class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0 # total amount
        last_minK = None # at initialization we dont have such elements
        last_maxK = None # at initialization we don't have such elements
        left_most = 0 # we have no elements before wich violates constraints, llb value

        for inx, n in enumerate(nums):
            if n < minK or n > maxK: # this elements violates constraints
                # last_minK and last_maxK cant be included in any window after inx
                left_most = inx+1
                last_minK = None
                last_maxK = None
            else:
                if n == minK:
                    last_minK = inx
                if n == maxK:
                    last_maxK = inx
                # we have both maxK and minK so lets calculate the number of subarrays ended at inx
                if last_minK is not None and last_maxK is not None:
                    right_most_left_border = min(last_minK, last_maxK)
                    count += right_most_left_border-left_most+1


        return count