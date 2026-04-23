class Solution:
	def maxSubArray(self, nums: List[int]) -> int:

		if len(nums) == 1:
			return nums[0]

		mn = 0
		mx = nums[0]
		s = 0
		#pref_sums.append(nums[i] + pref_sums[i])
		for i in range(len(nums)):
			s += nums[i]
			mx = max(mx, s - mn)
			mn = min(mn, s)
			
		
		# for i in range(len(pref_sums)):
		# 	mn = min(mn, pref_sums[i])
		# 	mx = max(mx, pref_sums[i] - mn)
		return mx
