class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        total_wage, total_quality, max_heap = float('inf'), 0, []
        for ratio, q in sorted([(w/q, q) for w, q in zip(wage, quality)]):
            total_quality += q
            heappush(max_heap, -q)
            if len(max_heap) == k:
                total_wage = min(total_wage, total_quality * ratio)
                total_quality += heappop(max_heap)
        return total_wage