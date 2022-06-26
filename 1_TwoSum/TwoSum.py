class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indxDict = {}
        for i,n in enumerate(nums):
            if (target - n) in indxDict:
                return [indxDict[target - n],i]
            indxDict[n] = i
        return []

# Loop through nums and check for pair to make target in dictionary. Add to dictionary if pair not found.
