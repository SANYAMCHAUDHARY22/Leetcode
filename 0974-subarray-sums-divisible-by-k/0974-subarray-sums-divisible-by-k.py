class Solution:
    # subarray [i, j] is divisible by k iff sum([0, j]) % k equals to
    # sum([0, i]) % k. this gives me idea to use hashtable. I hash
    # the remainders of sums at each index. Then we compare and count
    # them. I'd never write code like this at work though, completely
    # unreadable, 0 chance to pass the review...
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sums = [0]
        for n in nums: sums.append(sums[-1] + n)
        return sum([v * (v - 1) // 2 for v in Counter([n % k for n in sums]).values()])