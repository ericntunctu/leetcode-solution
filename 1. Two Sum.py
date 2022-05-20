class Solution:
  # idea: we just need a dictionary
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        s=dict()
        for i,x in enumerate(nums):
            s[x]=i
       
        
        ans=[]
        for i,x in enumerate(nums):
            if target-x in s and s[target-x]!=i:
                return [i, s[target-x]]
