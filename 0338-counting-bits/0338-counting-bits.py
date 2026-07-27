class Solution:
    def countBits(self, n: int) -> List[int]:
        """
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
        """
        """
        res = [0]c
        *(n+1)
        for i in range(n+1):
            n = i
            count = 0
            while n!=0:
                if n&1!=0:
                    count +=1
                n>>=1
            res[i] = count
        return res
        """
        res = [0]*(n+1)
        for i in range(1,n+1):
            res[i] = res[i>>1] + (i&1)
        return res


            



        