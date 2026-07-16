class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        d = {}
        max_count = float("-inf")
        for i in nums:
            d[i] = False
        for i in nums:
            next_ele = i+1
            prev_ele = i-1
            d[i] = True
            curr_len = 1

            while next_ele in d and d[next_ele] == False:
                curr_len += 1
                d[next_ele] = True
                next_ele+= 1
            while prev_ele in d and d[prev_ele] == False:
                curr_len += 1
                d[prev_ele] = True
                prev_ele -= 1
            
            max_count = max(max_count,curr_len)
        return max_count

        
