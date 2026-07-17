class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        res = ""
        guess_lis = list(guess)

        match_count = 0
        d = {}# 1:2
        for i in secret:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        count = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                d[secret[i]] -= 1
                guess_lis[i] = "*"
                if d[secret[i]] == 0:
                    del d[secret[i]]
                count += 1
        res += str(count)+"A"#1A

        cow_count = 0
        for i in guess_lis:
            if i in d:
                d[i] -=1
                cow_count+= 1
                if d[i] == 0:
                    del d[i]
        res += str(cow_count)+"B"

        return res
