class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.binsearch(nums,target,True)
        right=self.binsearch(nums,target,False)
        return [left,right]
    


    def binsearch(self,nums,target,leftbais):
        l,r=0,len(nums)-1
        i=-1
        while l<=r:
            m=(l+r)//2
            if nums[m]>target:
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                i=m
                if leftbais:
                    r=m-1
                else:
                    l=m+1
        return i
        