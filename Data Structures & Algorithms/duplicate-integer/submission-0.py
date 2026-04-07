class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(list(set(nums))):
            return False
        return True