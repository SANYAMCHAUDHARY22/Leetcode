class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = mask = 0
        freq = defaultdict(int, {0: 1})
        for ch in word: 
            mask ^= 1 << ord(ch)-97
            ans += freq[mask]
            for i in range(10): ans += freq[mask ^ 1 << i]
            freq[mask] += 1
        return ans 