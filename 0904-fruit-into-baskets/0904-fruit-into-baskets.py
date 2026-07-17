class Solution:
    def totalFruit(self, f: List[int]) -> int:
        d = {}
        l = 0
        maxi = float("-inf")
        for r in range(len(f)):
            if f[r] in d:
                d[f[r]] +=1
            else:
                d[f[r]] = 1
            
            while len(d) > 2:
                #maxi = max(maxi,r-l+1)
                d[f[l]] -= 1
                
                if d[f[l]] == 0:
                    del d[f[l]]
                l +=1
            maxi = max(maxi,sum(d.values()))
        return maxi



        