class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        s1 = set()
        l = 0
        maxi = float("-inf")
        for r in range(len(s)):
            while s[r] in s1:
                s1.remove(s[l])
                l += 1
            s1.add(s[r])
            maxi = max(maxi,r-l+1)

        return maxi
            
        