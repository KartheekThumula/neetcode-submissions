class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        a=len(set(nums))
        if n==a:
            return False
        else:
            return True
        