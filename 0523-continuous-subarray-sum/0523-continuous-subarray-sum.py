class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Create a dictionary to store the remainders and their corresponding indices
        remainder_dict = {0: -1}
        remainder = 0
        
        # Traverse through the list
        for i in range(len(nums)):
            # Update the remainder with the current number
            remainder += nums[i]
            
            # If k is not 0, take the remainder when divided by k
            if k != 0:
                remainder %= k
            
            # If the current remainder is already in the dictionary,
            # and the difference between the current index and the index
            # of the previous occurrence of the same remainder is at least 2,
            # we have found a subarray whose sum is a multiple of k
            if remainder in remainder_dict:
                if i - remainder_dict[remainder] >= 2:
                    return True
            else:
                # If the current remainder is not in the dictionary,
                # add it with its corresponding index
                remainder_dict[remainder] = i
        
        # If we have traversed through the whole list and haven't found a subarray,
        # return False
        return False