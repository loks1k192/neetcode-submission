class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		if len(nums) == 1:
			return nums[0]
		mn = 0
		s = 0
		mx = -10**6
		for i in range(len(nums)):
			s += nums[i]
			mx = max(mx, s - mn)
			mn = min(mn, s)
		return mx
