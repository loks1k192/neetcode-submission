class Solution:
	def maxSubArray(self, nums: List[int]) -> int:

		if len(nums) == 1:
			return nums[0]

		mn = 0
		mx = nums[0]

		#pref_sums.append(nums[i] + pref_sums[i])
		for i in range(len(nums)):
			
			mx = max(mx, sum(nums[:i+1]) - mn)
			mn = min(mn, sum(nums[:i+1]))
			
		
		# for i in range(len(pref_sums)):
		# 	mn = min(mn, pref_sums[i])
		# 	mx = max(mx, pref_sums[i] - mn)
		return mx
