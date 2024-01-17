class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        mini = nums[0]
        maxi = nums[-1]
        return gcd(mini,maxi)
        