class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        res = [0]*len(code)
        arr = code*2
        n = len(code)
        if k>0:
            window = sum(code[1:k+1])
            res[0] = window
            for i in range(1,len(code)):
                window += arr[i+k] 
                window -= arr[i]
                res[i] = window
        if k<0:
            #0 1 2 3 4 5 6 7
            #2 4 9 3 2 4 9 3
            #k = -k
            window = sum(arr[n+k:n])
            
            for i in range(n):
                res[i] = window
                window += arr[n+i]
                window -= arr[n+k+i]
        return res

        
            



        