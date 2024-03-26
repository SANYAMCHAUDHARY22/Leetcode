class Solution:
    def findDuplicates(self, N: List[int]) -> List[int]:
        S, A = set(), []
        for n in N:
            if n in S: A.append(n)
            else: S.add(n)
        return A
		