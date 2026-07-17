class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        maxi = max(len(v1),len(v2))
        for i in range(0,maxi):

            if i >= len(v1):
                a = 0
            else:
                a = int(v1[i])
            if i >= len(v2):
                b = 0
            else:
                b = int(v2[i])
            
            if a < b:
                return -1
            if a > b:
                return 1
        return 0
        