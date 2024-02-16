class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0)+1

        unique_elements = len(d)
        curr_deleted = 0
        count = 0
        for frequency in sorted(d.values()):
            curr_deleted += frequency
            count += 1
            if curr_deleted < k:
                continue
            elif curr_deleted == k:
                return unique_elements-count
            else:
                return unique_elements-(count-1)