class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        index=-1
        for i in range(n):
            if nums[i]==0:
                index=i
                break
        i=index
        while i<n:
            if nums[i]!=0:
                nums[index],nums[i]=nums[i],nums[index]
                i+=1
                index+=1
            else:
                i+=1
        return nums
                