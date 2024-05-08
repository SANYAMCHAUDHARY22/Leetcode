class Solution(object):
    def findRelativeRanks(self, score):
        # Create a dictionary to store each score's original index
        score_map = {score[i]: i for i in range(len(score))}

        # Sort the scores in descending order
        score.sort(reverse=True)

        # Create a result list to store the ranks
        result = ["" for _ in range(len(score))]
        for i in range(len(score)):
            # Assign ranks based on the position of each score in the sorted list
            if i == 0:
                result[score_map[score[i]]] = "Gold Medal"
            elif i == 1:
                result[score_map[score[i]]] = "Silver Medal"
            elif i == 2:
                result[score_map[score[i]]] = "Bronze Medal"
            else:
                result[score_map[score[i]]] = str(i + 1)

        return result