class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_new = set(t)
        d = {x : t.count(x) for x in t_new}
        res = '1' * (len(s) + 1)
        for i in range(len(s)):
            for j in range(len(s)):
                h = s[i: len(t) + i + j]
                if len(h) <= len(res):
                    if all(x in h for x in t):
                        if all(d[x] <= h.count(x) for x in t):
                            res = h
        if len(s) < len(t):
            return ''
        if s == t:
            return s
        return res if res != '1' * (len(s) + 1) else ''
