class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        seen = set()
        duplicates = None
        missing = None
        
        for i in nums:
            if i in seen:
                duplicates = i
            seen.add(i)
            
        for i in range(1,n+1):
            if i not in seen:
                missing = i
        return (duplicates,missing)
        