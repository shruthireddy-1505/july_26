class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = {}
        for i in p:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        d1 = {}
        res = []
        l = 0
        for r in range(len(s)):
            if s[r] in d1:
                d1[s[r]] += 1
            else:
                d1[s[r]] = 1
            
            if r-l+1 > len(p):
                d1[s[l]] -= 1

                if d1[s[l]] == 0:
                    del d1[s[l]]
                l += 1
            if d1 == d:
                res.append(l)
        return res