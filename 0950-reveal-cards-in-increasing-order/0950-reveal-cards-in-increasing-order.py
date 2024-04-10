class Solution:
    def deckRevealedIncreasing(self, D: List[int]) -> List[int]:
    	L, Q, _ = len(D)-1, collections.deque(), D.sort()
    	for _ in range(L): Q.appendleft(D.pop()), Q.appendleft(Q.pop())
    	return D + list(Q)