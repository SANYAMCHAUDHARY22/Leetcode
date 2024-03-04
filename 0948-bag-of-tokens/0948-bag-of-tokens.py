class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # play i-th token face up -> lose tokens[i] power -> choose the smallest one
        # play i-th token face down -> gain tokens[i] power -> choose the largest one
        # hence, sort tokens first
        tokens.sort()
        # two pointes - l for tracking face up & r for tracking face down
        l, r = 0, len(tokens) - 1
        cur_score = mx_score = 0
        while l <= r:
            # there are 3 cases
            if tokens[l] <= power:
                # case 1. play l-th tokens face up if its power <= the current power
                # ---
                # losing tokens[l] power
                power -= tokens[l]
                # and gaining 1 score
                cur_score += 1
                # cur_score can be mx_score potentially
                mx_score = max(mx_score, cur_score)
                # move the pointer to the right
                l += 1
            elif cur_score >= 1:
                # case 2. play r-th tokens face down if the current score is at least 1
                # ---
                # gaining tokens[r] power
                power += tokens[r]
                # and losing 1 score
                cur_score -= 1
                # move the pointer to the left
                r -= 1
            else:
                # case 3. impossible to play
                # ---
                # either you don't enough power or enough score
                break
        return mx_score