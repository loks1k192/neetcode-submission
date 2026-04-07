class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = []
        t = prices
        for i in range(1, len(prices)):
            t_cur = t[:i]
            t_next = t[i:]
            p.append(max(t_next) - min(t_cur))
        if len(prices) == 1:
            return 0
        return max(p) if max(p) > 0 else 0
