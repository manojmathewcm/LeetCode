class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_dict,t_dict = {},{}
        for i,j in zip(s,t):
            s_dict[i] = s_dict[i]+1 if s_dict.get(i) else 1
            t_dict[j] = t_dict[j]+1 if t_dict.get(j) else 1
        
        return (s_dict == t_dict)

# Map count of characters to dictionary and compare dictionaries
