class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        for c in t:
            if c not in s: return False
            s = s.replace(c,'',1)

        return True

# Loop through target and check/remove character from source
