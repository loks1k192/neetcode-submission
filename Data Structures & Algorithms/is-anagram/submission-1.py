class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {x:s.count(x) for x in set(s)}
        d2 = {x:t.count(x) for x in set(t)}
        if d1 == d2:
            return True
        return False