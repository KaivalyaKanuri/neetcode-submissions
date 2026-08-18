class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch = ''.join(sorted(s))
        jh  = ''.join(sorted(t))

        return ch == jh