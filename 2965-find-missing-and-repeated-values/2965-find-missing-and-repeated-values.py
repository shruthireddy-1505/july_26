class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        n = len(grid)
        m = len(grid[0])
        d = {}
        for i in range(n):
            for j in range(m):
                if grid[i][j] in d:
                    d[grid[i][j]] += 1
                else:
                    d[grid[i][j]] = 1
        
        maxi = n*n
        lis = []
        for i in range(1,maxi+1):
            lis.append(i)
        for k,v in d.items():
            if v == 2:
                ans.append(k)
                break
        for i in lis:
            if i not in d:
                ans.append(i)
                break
        
        return ans


        