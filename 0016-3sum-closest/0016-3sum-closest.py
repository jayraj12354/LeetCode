class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=float('-inf')
        mini=float('+inf')
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            
            while j<k:  
                # print(nums[i],nums[j],nums[k],"--->",nums[i]+nums[j]+nums[k],abs(nums[i]+nums[j]+nums[k]-target))
                if mini!=min(abs((nums[i]+nums[j]+nums[k])-target),mini):
                    ans=(nums[i]+nums[j]+nums[k])
                    mini=abs((nums[i]+nums[j]+nums[k])-target)
                
                # while j<k and  nums[j]==nums[j+1]:
                #     j+=1
                # while j<k and nums[k]==nums[k-1]:
                #     k-=1
                

                if j<k and (nums[i]+nums[j]+nums[k])<target:
                    j+=1
                elif j<k and (nums[i]+nums[j]+nums[k])>target:
                    k-=1
                elif j<k and (nums[i]+nums[j]+nums[k])==target:
                    return target
                
        
        return ans