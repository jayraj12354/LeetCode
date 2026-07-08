class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        arr=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=(-1)*nums[i]
            j=i+1
            k=len(nums)-1
            
            while j<k:
                if nums[j]+nums[k]==target:
                    arr.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and  nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif nums[j]+nums[k]>target:
                    k-=1
                elif nums[j]+nums[k]<target:
                    j+=1

        return arr

