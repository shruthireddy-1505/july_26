class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        for i in range(n+1):
            count = 0
            dup = i
            while i!=0:
                r = i%2
                if r == 1:
                    count +=1
                i = i //2
            res[dup] = count
        return res

        