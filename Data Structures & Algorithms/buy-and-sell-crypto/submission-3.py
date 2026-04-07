class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = float("+inf")
        mx = 0
        mn_indx = 0
        mx_indx = 0
        res = 0
        for i in range(0, len(prices)):
            if prices[i] < mn:
                mn = prices[i]
            elif prices[i] - mn > mx:
                mx = prices[i] - mn
                res = mx
        if len(prices) == 1:
            return 0
        return res if res > 0 else 0
