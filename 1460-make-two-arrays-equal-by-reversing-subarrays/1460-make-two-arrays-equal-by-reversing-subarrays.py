class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hash_target = defaultdict(int) # Counting HashMap for `target`
        hash_arr = defaultdict(int) # Counting HashMap for `arr`
        N = len(target)
        for i in range(N):
            hash_target[target[i]] += 1 # Hash each element of `target` and count its frequency
            hash_arr[arr[i]] += 1 # Hash each element of `arr` and count its frequency
        return hash_target == hash_arr # If elements of 2 arrays are the same and have same frequencies, then they can be equal