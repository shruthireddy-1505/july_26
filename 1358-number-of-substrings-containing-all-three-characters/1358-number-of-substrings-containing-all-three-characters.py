class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        d = {}
        count = 0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]] = 1
            while len(d) == 3:
                count += len(s)-i
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l+=1
        return count
        