class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td = {}
        res = ""
        min_len = float("inf")
        for i in t:
            if i in td:
                td[i]+=1
            else:
                td[i] = 1
        l = 0
        sd = {}
        count = 0
        for i in range(len(s)):
            if s[i] in t:
                if s[i] in sd:
                    sd[s[i]] +=1
                else:
                    sd[s[i]] = 1
                if s[i] in t and sd[s[i]] == td[s[i]]:
                    count += 1
                while count == len(td):
                    if i-l+1 < min_len:
                        min_len = i-l+1
                        res = s[l:i+1]
                    if s[l] in t:
                        sd[s[l]] -= 1
                        if sd[s[l]] < td[s[l]]:
                            count -=1
                        if sd[s[l]] == 0:
                            del sd[s[l]]
                    l += 1
        return res


