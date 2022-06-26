class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        for s_c,t_c in zip(sorted(list(s)),sorted(list(t))):
            if s_c != t_c: return False

        return True
 
# Loop through sorted source and target and compare elements
