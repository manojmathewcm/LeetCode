class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq = set()
        for n in nums:
            if n in uniq:
                return True
            else:
                uniq.add(n)
        return False

# Check for n in set and return true if already present, else add n to set
