class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        resDict = defaultdict(list)
        
        for s in strs:
            charMap = [0] * 26
            
            for char in s:
                charMap[ord(char) - ord('a')] += 1
            
            resDict[tuple(charMap)].append(s)
        
        return resDict.values()

# Add count of chars to map and add strings to dictionary with map as key
