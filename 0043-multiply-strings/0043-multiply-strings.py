class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        d1 = 0
        d2 = 0

        for i in num1:
            res = ord(i) - ord("0")
            d1 = d1*10+res

        for j in num2:
            ans = ord(j) - ord("0")
            d2 = d2*10+ans
        n = d1*d2
        res = ""
        while n!=0:
            r = n%10
            n//=10
            res = chr(ord('0')+r)+res
        return res
        