class Solution:
    def search(self,nums:List[int],target: int) -> int:
        if len(nums)==0:
            return False
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2

            if target==nums[mid]:
                return True

            #left sorted portion
            if nums[l] < nums[mid]:
                if target>nums[mid] or target<nums[l]:
                    #target is not in left portion
                    l=mid+1
                else:
                    #target is in left portion ,so bring the r in the left portion
                    r=mid-1
            elif nums[l] > nums[mid]:
                if target<nums[mid] or target>nums[r]:
                    #target is not in right portion 
                    r=mid-1
                else:
                    l=mid+1
            else:
                l+=1 # this basically for handling the condition of nums[l]==nums[mid]
        return False
