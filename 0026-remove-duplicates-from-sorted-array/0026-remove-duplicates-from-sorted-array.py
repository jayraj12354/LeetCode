class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # ans=sorted(list(set(nums)))+(len(nums)-len(sorted(list(set(nums)))))*["_"]
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                # print(nums)
                if nums[i]==nums[j]:
                    nums.pop(j)
                    continue
                j+=1
            i+=1
        



        return len(nums)