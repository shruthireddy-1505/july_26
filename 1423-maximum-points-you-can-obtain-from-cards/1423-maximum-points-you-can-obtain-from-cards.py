class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxi = float("-inf")
        curr_sum = 0
        n = len(cardPoints)
        for i in range(k):
            curr_sum += cardPoints[i]
        maxi = max(maxi,curr_sum)
        for i in range(k):
            curr_sum -= cardPoints[k-i-1]
            curr_sum += cardPoints[n-i-1]
            maxi = max(maxi,curr_sum)
        return maxi
        